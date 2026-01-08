"""
Test improved chatbot
Run: python manage.py shell < test_chatbot_improved.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eshop.settings')
django.setup()

print("=" * 70)
print("Testing Improved Chatbot")
print("=" * 70)

try:
    from store.ai_services import chatbot_service
    
    test_cases = [
        ("Hello", "Should greet"),
        ("trending products", "Should mention trending page"),
        ("Find electronics under 5000", "Should find electronics under 5000"),
        ("How do I track my order?", "Should explain tracking"),
        ("What categories do you have?", "Should list categories"),
        ("Show me headphones", "Should find headphones"),
        ("What's your return policy?", "Should explain returns"),
    ]
    
    for msg, expected in test_cases:
        print(f"\n{'='*70}")
        print(f"👤 User: {msg}")
        print(f"📝 Expected: {expected}")
        print(f"{'='*70}")
        
        response = chatbot_service.chat(msg, session_id="test-123")
        print(f"🤖 Bot Response:")
        print(f"   {response['response'][:200]}...")
        print(f"\n   Intent: {response['intent']}")
        
        if response['products']:
            print(f"   Products found: {len(response['products'])}")
            for p in response['products'][:3]:
                print(f"      • {p['title']} - ₹{p['price']}")
        
        # Check if response is appropriate
        if response['intent'] != 'unknown' or response['products']:
            print(f"   ✅ Response looks good!")
        else:
            print(f"   ⚠️  Might need improvement")
    
    print("\n" + "=" * 70)
    print("✅ Chatbot test complete!")
    print("=" * 70)
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
