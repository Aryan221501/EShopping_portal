"""
Quick test script to verify cart functionality
Run: python manage.py shell < test_cart.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eshop.settings')
django.setup()

from store.models import Product, Cart, CartItem

# Test cart creation
print("Testing cart functionality...")

# Get a product
product = Product.objects.first()
if product:
    print(f"Found product: {product.title}")
    
    # Create a test cart
    cart, created = Cart.objects.get_or_create(
        session_key='test-session-123'
    )
    print(f"Cart created: {created}, Cart ID: {cart.id}")
    
    # Add item to cart
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )
    print(f"Cart item created: {created}")
    print(f"Cart total: ₹{cart.get_total()}")
    print(f"Cart item count: {cart.get_item_count()}")
    print("\n✓ Cart functionality is working!")
else:
    print("No products found. Run: python manage.py populate_products")
