"""
Simple chatbot test
Run: python manage.py shell < test_chatbot_simple.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eshop.settings')
django.setup()

print("=" * 60)
print("Testing Chatbot")
print("=" * 60)

try:
    from store.ai_services import chatbot_service
    
    test_messages = [
        "Hello",
        "Find wireless headphones",
        "What's your shipping policy?",
        "help",
        "Show me electronics",
    ]
    
    for msg in test_messages:
        print(f"\n👤 User: {msg}")
        response = chatbot_service.chat(msg, session_id="test-123")
        print(f"🤖 Bot: {response['response']}")
        print(f"   Intent: {response['intent']}")
        if response['products']:
            print(f"   Products found: {len(response['products'])}")
            for p in response['products'][:2]:
                print(f"      - {p['title']} (₹{p['price']})")
    
    print("\n" + "=" * 60)
    print("✅ Chatbot is working!")
    print("=" * 60)
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
