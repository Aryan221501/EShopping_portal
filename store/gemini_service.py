"""
Gemini AI Integration for E-Shop Chatbot
Uses Google's Gemini API for intelligent, context-aware responses
"""
import os
import json
from typing import Dict, List
from django.core.cache import cache
from django.db.models import Q

# Gemini API will be imported when needed
_gemini_model = None

def get_gemini_model():
    """Lazy load Gemini model"""
    global _gemini_model
    if _gemini_model is None:
        try:
            import google.generativeai as genai
            
            # Get API key from environment
            api_key = os.getenv('GEMINI_API_KEY', '')
            if not api_key:
                print("⚠️ GEMINI_API_KEY not set in environment")
                return None
            
            genai.configure(api_key=api_key)
            _gemini_model = genai.GenerativeModel('gemini-pro')
            print("✓ Gemini AI model loaded")
        except Exception as e:
            print(f"Error loading Gemini: {e}")
            return None
    return _gemini_model



class GeminiChatbotService:
    """Gemini-powered chatbot for intelligent customer support"""
    
    def __init__(self):
        self.system_prompt = """You are a helpful AI shopping assistant for an e-commerce store called "AI E-Shop".

STORE INFORMATION:
- We sell: Electronics, Fashion, Beauty, Sports, Home & Kitchen, Books, Toys
- Free shipping on all orders
- 3-5 day delivery
- 30-day return policy
- Payment: Cash on Delivery (COD)
- Customer support available 24/7

YOUR ROLE:
- Help customers find products
- Answer questions about shipping, returns, payments
- Provide product recommendations
- Guide through checkout process
- Be friendly, concise, and helpful

GUIDELINES:
- Keep responses under 100 words
- Use emojis sparingly (1-2 per response)
- When customers ask about products, acknowledge and suggest they search
- For specific product queries, mention you'll search the catalog
- Always be positive and solution-oriented
"""
        self.conversation_history = {}
    
    def _search_products(self, query: str) -> List[Dict]:
        """Search products in database"""
        from .models import Product
        
        products = Product.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )[:5]
        
        return [
            {
                'id': p.id,
                'title': p.title,
                'price': str(p.price),
                'category': p.category.name,
                'description': p.description[:100]
            } for p in products
        ]

    
    def _extract_product_keywords(self, message: str) -> str:
        """Extract product search keywords from message"""
        stop_words = {'what', 'where', 'when', 'find', 'show', 'need', 'want', 
                     'looking', 'search', 'for', 'the', 'and', 'with', 'under', 
                     'below', 'above', 'less', 'than', 'more', 'get', 'buy', 'me', 'a', 'an'}
        
        words = message.lower().split()
        keywords = [w for w in words if len(w) > 2 and w not in stop_words and not w.isdigit()]
        return ' '.join(keywords[:3])  # Max 3 keywords
    
    def chat(self, message: str, session_id: str = None) -> Dict:
        """
        Process chat message using Gemini AI
        Returns: {'response': str, 'intent': str, 'products': list}
        """
        if not message or not message.strip():
            return {
                'response': "Please type a message! 😊",
                'intent': 'empty',
                'products': []
            }
        
        # Check cache first
        cache_key = f"gemini_chat_{hash(message)}"
        cached = cache.get(cache_key)
        if cached:
            return cached
        
        # Try to detect product search intent
        search_keywords = ['find', 'search', 'show', 'looking for', 'need', 'want', 'get', 'buy']
        is_product_search = any(keyword in message.lower() for keyword in search_keywords)
        
        products_found = []
        if is_product_search:
            keywords = self._extract_product_keywords(message)
            if keywords:
                products_found = self._search_products(keywords)
        
        # Get Gemini model
        model = get_gemini_model()
        
        if model is None:
            # Fallback to simple response
            if products_found:
                response = f"I found {len(products_found)} products for you! Check them out below."
            else:
                response = "I'm your AI shopping assistant! How can I help you today?"
            
            result = {
                'response': response,
                'intent': 'fallback',
                'products': products_found
            }
        else:
            try:
                # Build context
                context = self.system_prompt
                
                if products_found:
                    context += f"\n\nPRODUCTS FOUND: {len(products_found)} products matching the query."
                
                # Get conversation history
                if session_id:
                    history = self.conversation_history.get(session_id, [])
                    if history:
                        context += "\n\nRECENT CONVERSATION:\n"
                        for msg in history[-3:]:  # Last 3 messages
                            context += f"User: {msg['user']}\nAssistant: {msg['assistant']}\n"
                
                # Generate response
                full_prompt = f"{context}\n\nUser: {message}\nAssistant:"
                
                response = model.generate_content(full_prompt)
                ai_response = response.text.strip()
                
                # Update conversation history
                if session_id:
                    if session_id not in self.conversation_history:
                        self.conversation_history[session_id] = []
                    self.conversation_history[session_id].append({
                        'user': message,
                        'assistant': ai_response
                    })
                    # Keep only last 10 messages
                    self.conversation_history[session_id] = self.conversation_history[session_id][-10:]
                
                result = {
                    'response': ai_response,
                    'intent': 'gemini_ai',
                    'products': products_found
                }
                
            except Exception as e:
                print(f"Gemini error: {e}")
                result = {
                    'response': "I'm here to help! What would you like to know about our products?",
                    'intent': 'error',
                    'products': products_found
                }
        
        # Cache for 5 minutes
        cache.set(cache_key, result, 300)
        return result


# Global instance
gemini_chatbot = GeminiChatbotService()
