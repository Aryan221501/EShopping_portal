"""
Test AI Features
Run: python manage.py shell < test_ai_features.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eshop.settings')
django.setup()

print("=" * 50)
print("Testing AI Features")
print("=" * 50)

# Test 1: Chatbot
print("\n1. Testing Chatbot...")
try:
    from store.ai_services import chatbot_service
    
    test_messages = [
        "Hello",
        "Find wireless headphones",
        "What's your shipping policy?",
        "Show me products under 2000"
    ]
    
    for msg in test_messages:
        response = chatbot_service.chat(msg)
        print(f"   Q: {msg}")
        print(f"   A: {response['response'][:80]}...")
        print(f"   Intent: {response['intent']}")
        print()
    
    print("   ✓ Chatbot working!")
except Exception as e:
    print(f"   ✗ Chatbot error: {e}")

# Test 2: TF-IDF Recommendations
print("\n2. Testing TF-IDF Recommendations...")
try:
    from store.ai_services import recommendation_service
    from store.models import Product
    
    product = Product.objects.first()
    if product:
        recs = recommendation_service.get_similar_products_tfidf(product.id, limit=5)
        print(f"   Product: {product.title}")
        print(f"   Found {len(recs)} recommendations")
        print("   ✓ TF-IDF recommendations working!")
    else:
        print("   ✗ No products found. Run: python manage.py populate_products")
except Exception as e:
    print(f"   ✗ TF-IDF error: {e}")

# Test 3: Trending Products
print("\n3. Testing Trending Products...")
try:
    trending = recommendation_service.get_trending_products(limit=5)
    print(f"   Found {len(trending)} trending products")
    print("   ✓ Trending products working!")
except Exception as e:
    print(f"   ✗ Trending error: {e}")

# Test 4: Hybrid Recommendations
print("\n4. Testing Hybrid Recommendations...")
try:
    from store.models import Product
    product = Product.objects.first()
    if product:
        hybrid_recs = recommendation_service.get_hybrid_recommendations(product.id, limit=5)
        print(f"   Product: {product.title}")
        print(f"   Found {len(hybrid_recs)} hybrid recommendations")
        print("   ✓ Hybrid recommendations working!")
except Exception as e:
    print(f"   ✗ Hybrid error: {e}")

print("\n" + "=" * 50)
print("AI Features Test Complete!")
print("=" * 50)
print("\nNote: Some features require AI models to be installed.")
print("Run: install_ai.bat (Windows) or pip install -r requirements.txt")
print("\nVisit:")
print("  - Chatbot: http://127.0.0.1:8000/chatbot/")
print("  - Trending: http://127.0.0.1:8000/trending/")
print("  - Any product page for AI recommendations")
