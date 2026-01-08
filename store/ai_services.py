"""
AI Services for E-Shop
- Chatbot using Hugging Face transformers
- Advanced recommendations using TF-IDF and embeddings
"""
import os
import json
from typing import List, Dict, Tuple
from django.core.cache import cache
from django.db.models import Count, Q
import numpy as np

# Lazy imports to avoid loading models on every request
_chatbot_model = None
_chatbot_tokenizer = None
_sentence_model = None
_tfidf_vectorizer = None
_tfidf_matrix = None

def get_chatbot_model():
    """Lazy load chatbot model (DialoGPT-small for speed)"""
    global _chatbot_model, _chatbot_tokenizer
    if _chatbot_model is None:
        try:
            from transformers import AutoModelForCausalLM, AutoTokenizer
            import torch
            print("Loading fast chatbot model...")
            model_name = "microsoft/DialoGPT-small"  # Faster than medium
            _chatbot_tokenizer = AutoTokenizer.from_pretrained(model_name)
            _chatbot_model = AutoModelForCausalLM.from_pretrained(model_name)
            _chatbot_tokenizer.pad_token = _chatbot_tokenizer.eos_token
            print("✓ Fast chatbot model loaded")
        except Exception as e:
            print(f"Error loading chatbot: {e}")
            return None, None
    return _chatbot_model, _chatbot_tokenizer

def get_sentence_model():
    """Lazy load sentence transformer for embeddings"""
    global _sentence_model
    if _sentence_model is None:
        try:
            from sentence_transformers import SentenceTransformer
            print("Loading sentence transformer...")
            _sentence_model = SentenceTransformer('all-MiniLM-L6-v2')  # Fast, lightweight
            print("✓ Sentence model loaded")
        except Exception as e:
            print(f"Error loading sentence model: {e}")
            return None
    return _sentence_model


class ChatbotService:
    """AI Chatbot for customer support with GPT-style responses"""
    
    def __init__(self):
        self.context_cache = {}
        self.conversation_history = {}
        self.intents = self._load_intents()
        self.system_context = """You are a helpful AI shopping assistant for an e-commerce store. 
You help customers find products, answer questions about shipping, returns, payments, and provide excellent customer service.
Be friendly, concise, and helpful. When customers ask about products, search the catalog and show relevant items.
Store policies: Free shipping on all orders, 3-5 day delivery, 30-day returns, Cash on Delivery available."""
    
    def _load_intents(self) -> Dict:
        """Load predefined intents and responses"""
        return {
            'greeting': {
                'patterns': ['hi', 'hello', 'hey', 'good morning', 'good evening', 'hola', 'namaste'],
                'responses': [
                    "Hello! 👋 Welcome to AI E-Shop. How can I help you today?",
                    "Hi there! I'm your AI shopping assistant. What are you looking for?",
                    "Hey! Looking for something specific? I can help you find products, answer questions, or guide you through checkout."
                ]
            },
            'help': {
                'patterns': ['help', 'what can you do', 'how to use', 'assist', 'support'],
                'responses': [
                    "I can help you with:\n• Finding products (try: 'find wireless headphones')\n• Shipping info\n• Return policy\n• Payment methods\n• Checkout process\n\nJust ask me anything!",
                    "Here's what I can do:\n✓ Search products\n✓ Answer questions about shipping & returns\n✓ Help with checkout\n✓ Recommend products\n\nWhat would you like to know?",
                ]
            },
            'product_search': {
                'patterns': ['find', 'search', 'looking for', 'need', 'want', 'show me', 'get me', 'buy'],
                'responses': [
                    "I can help you find products! What are you looking for?",
                    "Sure! Tell me what kind of product you need.",
                    "I'd be happy to help you search. What category interests you?"
                ]
            },
            'categories': {
                'patterns': ['categories', 'what do you sell', 'what products', 'types of products'],
                'responses': [
                    "We have products in these categories:\n• Electronics\n• Fashion\n• Home & Kitchen\n• Books\n• Sports\n• Beauty\n• Toys\n\nWhat interests you?",
                    "Our store offers:\n✓ Electronics (headphones, chargers, etc.)\n✓ Fashion (clothing, shoes, accessories)\n✓ Home & Kitchen\n✓ Books\n✓ Sports equipment\n✓ Beauty products\n✓ Toys\n\nTell me what you're looking for!",
                ]
            },
            'price_query': {
                'patterns': ['price', 'cost', 'how much', 'expensive', 'cheap', 'budget'],
                'responses': [
                    "I can help you find products in your budget. What's your price range?",
                    "We have products at various price points. What's your budget?",
                    "Let me help you find affordable options. What price range works for you?"
                ]
            },
            'cart_help': {
                'patterns': ['cart', 'checkout', 'order', 'buy', 'purchase'],
                'responses': [
                    "To add items to cart, click 'Add to Cart' on any product page.",
                    "You can view your cart by clicking the cart icon in the navigation bar.",
                    "Ready to checkout? Click on the cart icon and then 'Proceed to Checkout'."
                ]
            },
            'shipping': {
                'patterns': ['shipping', 'delivery', 'when will', 'how long'],
                'responses': [
                    "We offer free shipping on all orders! Delivery takes 3-5 business days.",
                    "Your order will be delivered within 3-5 business days.",
                    "We provide free shipping with estimated delivery in 3-5 business days."
                ]
            },
            'tracking': {
                'patterns': ['track', 'tracking', 'where is my order', 'order status'],
                'responses': [
                    "To track your order, go to your order confirmation email and click the tracking link. You can also check order status in your account.",
                    "You can track your order using the tracking number sent to your email after purchase.",
                    "Order tracking information is available in your order confirmation email and account dashboard."
                ]
            },
            'return_policy': {
                'patterns': ['return', 'refund', 'exchange', 'money back'],
                'responses': [
                    "We have a 30-day return policy. Contact support for returns.",
                    "You can return products within 30 days of purchase.",
                    "We offer hassle-free returns within 30 days."
                ]
            },
            'payment': {
                'patterns': ['payment', 'pay', 'credit card', 'debit', 'upi', 'cod'],
                'responses': [
                    "We accept Cash on Delivery (COD). More payment options coming soon!",
                    "Currently, we support Cash on Delivery. Credit card and UPI coming soon!",
                    "You can pay via Cash on Delivery when your order arrives."
                ]
            },
            'recommendation': {
                'patterns': ['recommend', 'suggest', 'best', 'popular'],
                'responses': [
                    "I can recommend products based on your interests! What category do you like?",
                    "Our AI can suggest personalized products. What are you interested in?",
                    "Let me help you discover great products! What's your preference?"
                ]
            },
            'trending': {
                'patterns': ['trending', 'hot', 'whats popular', 'most viewed', 'bestseller', 'top selling'],
                'responses': [
                    "Check out our trending products page at /trending/ to see what's hot right now!",
                    "Want to see trending products? Visit our Trending page in the navigation menu!",
                    "Our most popular products are on the Trending page. Click 'Trending' in the menu above!"
                ]
            },
            'about_store': {
                'patterns': ['about', 'who are you', 'your store', 'tell me about', 'what is this'],
                'responses': [
                    "We're an AI-powered e-commerce store offering electronics, fashion, beauty, sports, home & kitchen, appliances, books, and toys. We provide free shipping, 30-day returns, and excellent customer service!",
                    "Welcome to our online store! We offer a wide range of products with free shipping, easy returns, and AI-powered shopping assistance. Browse our catalog or ask me to find something specific!",
                ]
            },
            'thanks': {
                'patterns': ['thank', 'thanks', 'appreciate', 'helpful'],
                'responses': [
                    "You're welcome! Happy to help. Let me know if you need anything else!",
                    "Glad I could help! Feel free to ask if you have more questions.",
                    "My pleasure! Enjoy shopping with us!"
                ]
            },
            'goodbye': {
                'patterns': ['bye', 'goodbye', 'see you', 'later'],
                'responses': [
                    "Goodbye! Come back anytime. Happy shopping!",
                    "See you later! Don't hesitate to return if you need help.",
                    "Bye! Thanks for visiting. Have a great day!"
                ]
            }
        }
    
    def _match_intent(self, message: str) -> Tuple[str, str]:
        """Match user message to intent"""
        message_lower = message.lower()
        
        for intent_name, intent_data in self.intents.items():
            for pattern in intent_data['patterns']:
                if pattern in message_lower:
                    import random
                    response = random.choice(intent_data['responses'])
                    return intent_name, response
        
        return 'unknown', None
    
    def _search_products(self, query: str) -> str:
        """Search products and return formatted response"""
        from .models import Product
        
        products = Product.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )[:5]
        
        if products:
            response = f"I found {products.count()} products matching '{query}':\n\n"
            for p in products:
                response += f"• {p.title} - ₹{p.price}\n"
            response += "\nClick on any product to view details!"
            return response
        else:
            return f"Sorry, I couldn't find products matching '{query}'. Try different keywords!"
    
    def _generate_ai_response(self, message: str, session_id: str = None) -> str:
        """Generate AI response using DialoGPT (optimized for speed)"""
        try:
            # Check cache first
            cache_key = f"ai_response_{hash(message)}"
            cached = cache.get(cache_key)
            if cached:
                return cached
            
            model, tokenizer = get_chatbot_model()
            if model is None or tokenizer is None:
                return None
            
            # Simplified: Use only current message for speed
            input_ids = tokenizer.encode(message + tokenizer.eos_token, return_tensors='pt')
            
            # Fast generation with reduced parameters
            import torch
            with torch.no_grad():
                output = model.generate(
                    input_ids,
                    max_length=input_ids.shape[1] + 30,  # Shorter responses
                    num_return_sequences=1,
                    no_repeat_ngram_size=2,
                    do_sample=False,  # Greedy = faster
                    pad_token_id=tokenizer.eos_token_id,
                    early_stopping=True
                )
            
            # Decode response
            response = tokenizer.decode(output[0][input_ids.shape[1]:], skip_special_tokens=True)
            response = response.strip()
            
            # Cache for 5 minutes
            cache.set(cache_key, response, 300)
            
            return response
            
        except Exception as e:
            print(f"AI generation error: {e}")
            return None
    
    def _enhance_response_with_context(self, base_response: str, intent: str, products: list) -> str:
        """Enhance response with store-specific context"""
        enhancements = {
            'greeting': " I can help you find products, answer questions about shipping and returns, or guide you through checkout. What would you like to know?",
            'shipping': " We offer free shipping on all orders with delivery in 3-5 business days.",
            'return_policy': " You can return any product within 30 days of purchase for a full refund.",
            'payment': " We currently accept Cash on Delivery (COD). Credit card and UPI options coming soon!",
            'tracking': " You'll receive a tracking number via email once your order ships.",
        }
        
        if intent in enhancements and enhancements[intent] not in base_response:
            base_response += enhancements[intent]
        
        return base_response
    
    def chat(self, message: str, session_id: str = None) -> Dict:
        """
        Process chat message and return response
        Returns: {'response': str, 'intent': str, 'products': list}
        """
        if not message or not message.strip():
            return {
                'response': "Please type a message!",
                'intent': 'empty',
                'products': []
            }
        
        # First, check for product search intent
        stop_words = ['what', 'where', 'when', 'find', 'show', 'need', 'want', 'looking', 
                     'search', 'for', 'the', 'and', 'with', 'under', 'below', 'above', 
                     'less', 'than', 'more', 'price', 'cost', 'rupees', 'inr', 'get', 'buy']
        
        # Extract price if mentioned
        price_limit = None
        words = message.lower().split()
        for word in words:
            if word.isdigit() and len(word) >= 3:
                price_limit = int(word)
                break
        
        # Filter keywords for product search
        keywords = [word for word in words 
                   if len(word) > 2 and word not in stop_words and not word.isdigit()]
        
        # Try to find products
        products_found = []
        if keywords:
            search_query = ' '.join(keywords)
            from .models import Product
            products = Product.objects.filter(
                Q(title__icontains=search_query) | 
                Q(description__icontains=search_query) |
                Q(category__name__icontains=search_query)
            )
            
            if price_limit:
                products = products.filter(price__lte=price_limit)
            
            products = products[:5]
            products_found = list(products)
        
        # Match intent for known patterns
        intent, pattern_response = self._match_intent(message)
        
        # Generate AI response
        ai_response = None
        if intent == 'unknown' or not pattern_response:
            ai_response = self._generate_ai_response(message, session_id)
        
        # Build final response
        if products_found:
            # Product search successful
            if price_limit:
                response = f"Great! I found {len(products_found)} products matching '{search_query}' under ₹{price_limit}:\n\n"
            else:
                response = f"Perfect! Here are {len(products_found)} products matching '{search_query}':\n\n"
            
            for p in products_found:
                response += f"• {p.title} - ₹{p.price}\n"
            response += "\nClick on any product card below to view full details and add to cart!"
            
            result = {
                'response': response,
                'intent': 'product_search',
                'products': [
                    {
                        'id': p.id,
                        'title': p.title,
                        'price': str(p.price),
                        'category': p.category.name
                    } for p in products_found
                ]
            }
        elif pattern_response:
            # Known intent with pattern response
            response = self._enhance_response_with_context(pattern_response, intent, [])
            result = {
                'response': response,
                'intent': intent,
                'products': []
            }
        elif ai_response:
            # AI generated response
            result = {
                'response': ai_response,
                'intent': 'ai_generated',
                'products': []
            }
        else:
            # Fallback
            result = {
                'response': "I'm your AI shopping assistant! I can help you:\n\n• Find products (try: 'show me laptops under 50000')\n• Answer questions about shipping, returns, and payments\n• Guide you through checkout\n• Recommend products\n\nWhat would you like to know?",
                'intent': 'help',
                'products': []
            }
        
        return result


class AdvancedRecommendationService:
    """Advanced recommendation system using TF-IDF and embeddings"""
    
    def __init__(self):
        self.tfidf_vectorizer = None
        self.tfidf_matrix = None
        self.product_embeddings = None
    
    def _build_tfidf_matrix(self):
        """Build TF-IDF matrix for all products"""
        from .models import Product
        from sklearn.feature_extraction.text import TfidfVectorizer
        
        cache_key = 'tfidf_matrix'
        cached = cache.get(cache_key)
        
        if cached:
            self.tfidf_vectorizer, self.tfidf_matrix = cached
            return
        
        products = Product.objects.all()
        if not products:
            return
        
        # Combine title and description
        documents = [
            f"{p.title} {p.description} {p.category.name}"
            for p in products
        ]
        
        self.tfidf_vectorizer = TfidfVectorizer(
            max_features=500,
            stop_words='english',
            ngram_range=(1, 2)
        )
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(documents)
        
        # Cache for 1 hour
        cache.set(cache_key, (self.tfidf_vectorizer, self.tfidf_matrix), 3600)
    
    def get_similar_products_tfidf(self, product_id: int, limit: int = 10) -> List[int]:
        """Get similar products using TF-IDF cosine similarity"""
        from .models import Product
        from sklearn.metrics.pairwise import cosine_similarity
        
        cache_key = f'tfidf_rec_{product_id}'
        cached = cache.get(cache_key)
        if cached:
            return cached
        
        self._build_tfidf_matrix()
        
        if self.tfidf_matrix is None:
            return []
        
        products = list(Product.objects.all())
        try:
            product_idx = [p.id for p in products].index(product_id)
        except ValueError:
            return []
        
        # Calculate cosine similarity
        similarities = cosine_similarity(
            self.tfidf_matrix[product_idx:product_idx+1],
            self.tfidf_matrix
        ).flatten()
        
        # Get top similar products (excluding self)
        similar_indices = similarities.argsort()[::-1][1:limit+1]
        similar_ids = [products[idx].id for idx in similar_indices]
        
        # Cache for 10 minutes
        cache.set(cache_key, similar_ids, 600)
        return similar_ids
    
    def get_similar_products_embeddings(self, product_id: int, limit: int = 10) -> List[int]:
        """Get similar products using sentence embeddings"""
        from .models import Product
        from sklearn.metrics.pairwise import cosine_similarity
        
        cache_key = f'embed_rec_{product_id}'
        cached = cache.get(cache_key)
        if cached:
            return cached
        
        model = get_sentence_model()
        if model is None:
            return self.get_similar_products_tfidf(product_id, limit)
        
        products = list(Product.objects.all())
        try:
            product_idx = [p.id for p in products].index(product_id)
        except ValueError:
            return []
        
        # Get or create embeddings
        embeddings_key = 'product_embeddings'
        embeddings = cache.get(embeddings_key)
        
        if embeddings is None:
            texts = [f"{p.title} {p.description}" for p in products]
            embeddings = model.encode(texts)
            cache.set(embeddings_key, embeddings, 3600)  # Cache 1 hour
        
        # Calculate similarity
        similarities = cosine_similarity(
            embeddings[product_idx:product_idx+1],
            embeddings
        ).flatten()
        
        # Get top similar products
        similar_indices = similarities.argsort()[::-1][1:limit+1]
        similar_ids = [products[idx].id for idx in similar_indices]
        
        cache.set(cache_key, similar_ids, 600)
        return similar_ids
    
    def get_collaborative_recommendations(self, user_id: int = None, limit: int = 10) -> List[int]:
        """Get recommendations based on user behavior (collaborative filtering)"""
        from .models import Product, BehaviorLog
        from django.db.models import Count
        
        if not user_id:
            # Return popular products for anonymous users
            return list(
                Product.objects.annotate(
                    view_count=Count('behaviorlog')
                ).order_by('-view_count')[:limit].values_list('id', flat=True)
            )
        
        # Get products user has interacted with
        user_products = BehaviorLog.objects.filter(
            user_id=user_id
        ).values_list('product_id', flat=True)
        
        if not user_products:
            return self.get_trending_products(limit)
        
        # Find similar users (users who viewed same products)
        similar_users = BehaviorLog.objects.filter(
            product_id__in=user_products
        ).exclude(user_id=user_id).values_list('user_id', flat=True).distinct()
        
        # Get products those users liked
        recommended_products = BehaviorLog.objects.filter(
            user_id__in=similar_users
        ).exclude(
            product_id__in=user_products
        ).values('product_id').annotate(
            score=Count('id')
        ).order_by('-score')[:limit]
        
        return [item['product_id'] for item in recommended_products]
    
    def get_trending_products(self, limit: int = 10) -> List[int]:
        """Get trending products based on recent activity"""
        from .models import Product, BehaviorLog
        from django.utils import timezone
        from datetime import timedelta
        
        cache_key = 'trending_products'
        cached = cache.get(cache_key)
        if cached:
            return cached
        
        # Get products with most activity in last 7 days
        week_ago = timezone.now() - timedelta(days=7)
        trending = BehaviorLog.objects.filter(
            timestamp__gte=week_ago
        ).values('product_id').annotate(
            score=Count('id')
        ).order_by('-score')[:limit]
        
        result = [item['product_id'] for item in trending]
        cache.set(cache_key, result, 300)  # Cache 5 minutes
        return result
    
    def get_hybrid_recommendations(self, product_id: int, user_id: int = None, limit: int = 10) -> List[int]:
        """Hybrid recommendations combining multiple methods"""
        # Get recommendations from different methods
        tfidf_recs = self.get_similar_products_tfidf(product_id, limit)
        embed_recs = self.get_similar_products_embeddings(product_id, limit)
        
        # Combine with weighted scoring
        scores = {}
        
        # TF-IDF recommendations (weight: 0.4)
        for i, pid in enumerate(tfidf_recs):
            scores[pid] = scores.get(pid, 0) + (limit - i) * 0.4
        
        # Embedding recommendations (weight: 0.6)
        for i, pid in enumerate(embed_recs):
            scores[pid] = scores.get(pid, 0) + (limit - i) * 0.6
        
        # Sort by score
        sorted_products = sorted(scores.items(), key=lambda x: -x[1])
        return [pid for pid, score in sorted_products[:limit]]


# Global instances
chatbot_service = ChatbotService()
recommendation_service = AdvancedRecommendationService()
