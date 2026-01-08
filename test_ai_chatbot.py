"""
Test AI-powered chatbot with real GPT-style responses
Run: python manage.py shell < test_ai_chatbot.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eshop.settings')
django.setup()

print("=" * 70)
print("Testing AI-Powered Chatbot (DialoGPT)")
print("=" * 70)
print("\nNote: First run will download the model (~350MB)")
print("This may take 2-3 minutes...\n")

try:
    from store.ai_services import chatbot_service
    
    test_queries = [
        "Hello, I'm looking for a new phone",
        "What phones do you have under 50000?",
        "Tell me about the iPhone",
        "What's your return policy?",
        "How long does shipping take?",
        "Show me some laptops",
        "I need headphones for gym",
        "What payment methods do you accept?",
    ]
    
    session_id = "test-session-123"
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n{'='*70}")
        print(f"Query {i}: {query}")
        print(f"{'='*70}")
        
        response = chatbot_service.chat(query, session_id=session_id)
        
        print(f"\n🤖 AI Response:")
        print(f"{response['response']}\n")
        
        if response['products']:
            print(f"📦 Products Found: {len(response['products'])}")
            for p in response['products'][:3]:
                print(f"   • {p['title']} - ₹{p['price']}")
        
        print(f"\n💡 Intent: {response['intent']}")
    
    print("\n" + "=" * 70)
    print("✅ AI Chatbot Test Complete!")
    print("=" * 70)
    print("\nThe chatbot now uses DialoGPT for intelligent responses!")
    print("It maintains conversation context and generates natural replies.")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
    print("\nIf you see 'No module named transformers', run:")
    print("pip install transformers torch")
