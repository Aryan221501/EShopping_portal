# Debug Instructions for Cart & Checkout

## Quick Fix Steps

### Step 1: Ensure migrations are applied
```bash
cd ai_eshop_project
python manage.py migrate
```

### Step 2: Start the server
```bash
python manage.py runserver
```

### Step 3: Test in browser
1. Open: http://127.0.0.1:8000/
2. Click on any product
3. Click "Add to Cart" button
4. Watch the browser console (F12) for errors

---

## What to Check

### In Browser Console (F12):
Look for these errors:
- ❌ **403 Forbidden** → CSRF issue (already fixed in settings)
- ❌ **404 Not Found** → URL routing issue
- ❌ **500 Server Error** → Check terminal for Python errors
- ✅ **200 OK** → Working correctly!

### In Terminal (where runserver is running):
Look for:
- Python exceptions
- Database errors
- Import errors

---

## Manual Test

### Test 1: Visit cart page directly
```
http://127.0.0.1:8000/cart/
```
Should show empty cart or items if any exist.

### Test 2: Test API endpoint
```
http://127.0.0.1:8000/api/cart/count/
```
Should return: `{"count": 0}` or similar JSON

### Test 3: Add product via Python shell
```bash
python manage.py shell
```

```python
from store.models import Product, Cart, CartItem

# Create a cart
cart = Cart.objects.create(session_key='manual-test-123')
print(f"✓ Cart created: ID={cart.id}")

# Get first product
product = Product.objects.first()
print(f"✓ Product: {product.title}")

# Add to cart
item = CartItem.objects.create(
    cart=cart,
    product=product,
    quantity=1
)
print(f"✓ Added to cart: {item.product.title}")
print(f"✓ Cart total: ₹{cart.get_total()}")
print(f"✓ Item count: {cart.get_item_count()}")

print("\n✅ Cart system is working!")
```

---

## Common Issues & Solutions

### Issue: "Add to Cart" button does nothing

**Check 1**: Browser console errors
- Open F12 → Console tab
- Click "Add to Cart"
- Look for red errors

**Check 2**: Is JavaScript loading?
- View page source (Ctrl+U)
- Search for "addToCart"
- Should find the function

**Check 3**: CSRF token
- In browser console, type:
```javascript
document.cookie
```
- Should see `csrftoken=...`

### Issue: Checkout page shows error

**Most likely**: Template variable error

**Fix**: Check terminal for exact error message, it will show:
```
TemplateDoesNotExist: store/checkout.html
or
AttributeError: 'Cart' object has no attribute 'items'
```

---

## Force Refresh Everything

```bash
# Stop server (Ctrl+C)

# Clear Python cache
python manage.py clean_pyc  # if available
# or manually delete __pycache__ folders

# Restart server
python manage.py runserver

# In browser:
# - Clear cache (Ctrl+Shift+Delete)
# - Hard refresh (Ctrl+F5)
```

---

## Test URLs

After starting server, test these URLs:

1. ✅ Home: http://127.0.0.1:8000/
2. ✅ Product: http://127.0.0.1:8000/product/1/
3. ✅ Cart: http://127.0.0.1:8000/cart/
4. ✅ Search: http://127.0.0.1:8000/search/?q=phone
5. ✅ API Products: http://127.0.0.1:8000/api/products/
6. ✅ API Cart Count: http://127.0.0.1:8000/api/cart/count/

All should load without 404 or 500 errors.

---

## If Still Not Working

### Option 1: Check exact error
1. Click "Add to Cart"
2. Open browser console (F12)
3. Copy the exact error message
4. Share it for specific help

### Option 2: Check server logs
1. Look at terminal where `runserver` is running
2. Copy any error messages
3. Share for specific help

### Option 3: Test with different browser
- Try Chrome, Firefox, or Edge
- Sometimes browser extensions block requests

---

## Success Indicators

You'll know it's working when:
1. ✅ Cart badge shows number in navbar
2. ✅ "Add to Cart" button shows "Added!" briefly
3. ✅ Cart page shows added products
4. ✅ Checkout page loads with form
5. ✅ Order confirmation shows after checkout

---

## Need More Help?

Provide these details:
1. Exact error message from browser console
2. Error from terminal (if any)
3. Which step fails (add to cart, view cart, checkout)
4. Browser and version
5. Python and Django versions
