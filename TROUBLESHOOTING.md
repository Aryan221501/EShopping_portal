# Troubleshooting Guide

## Cart & Checkout Issues - Quick Fixes

### Issue 1: "Add to Cart" not working

**Possible causes:**
1. Migrations not applied
2. Session not configured
3. CSRF token issues
4. JavaScript errors

**Solutions:**

#### Step 1: Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Step 2: Clear browser cache and cookies
- Press Ctrl+Shift+Delete
- Clear cookies and cached files
- Restart browser

#### Step 3: Check browser console for errors
- Press F12 to open Developer Tools
- Go to Console tab
- Look for red error messages
- Common errors:
  - "CSRF token missing" → Clear cookies
  - "403 Forbidden" → Check CSRF_TRUSTED_ORIGINS in settings
  - "Network error" → Check if server is running

#### Step 4: Test cart manually
```bash
python manage.py shell
```
Then run:
```python
from store.models import Product, Cart, CartItem

# Get a product
product = Product.objects.first()
print(f"Product: {product.title}")

# Create cart
cart = Cart.objects.create(session_key='test-123')
print(f"Cart created: {cart.id}")

# Add item
item = CartItem.objects.create(cart=cart, product=product, quantity=1)
print(f"Item added: {item.product.title}")
print(f"Cart total: ₹{cart.get_total()}")
```

### Issue 2: Checkout page throwing error

**Common errors and fixes:**

#### Error: "Cart object has no attribute 'items'"
**Fix**: Migrations not applied
```bash
python manage.py migrate store
```

#### Error: "CSRF verification failed"
**Fix**: Add to settings.py:
```python
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://127.0.0.1:8000']
```

#### Error: "Session key is None"
**Fix**: Ensure session middleware is enabled in settings.py:
```python
MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
]
```

### Issue 3: Cart count not updating

**Fix**: Check if JavaScript is loading
1. Open browser console (F12)
2. Type: `fetch('/api/cart/count/')`
3. Should return: `{count: 0}` or similar

If error, check:
- Server is running
- URL is correct
- CORS settings (if using different domain)

---

## Quick Test Commands

### Test 1: Check if models are working
```bash
python manage.py shell
```
```python
from store.models import *
print(f"Products: {Product.objects.count()}")
print(f"Carts: {Cart.objects.count()}")
print(f"Orders: {Order.objects.count()}")
```

### Test 2: Create a test order
```bash
python manage.py shell
```
```python
from store.models import *
from decimal import Decimal

# Create cart
cart = Cart.objects.create(session_key='test-order-123')

# Add items
product = Product.objects.first()
CartItem.objects.create(cart=cart, product=product, quantity=2)

# Check total
print(f"Cart total: ₹{cart.get_total()}")
print(f"Items: {cart.get_item_count()}")
```

### Test 3: Test AJAX endpoints
Open browser and visit:
- http://127.0.0.1:8000/api/products/
- http://127.0.0.1:8000/api/categories/
- http://127.0.0.1:8000/api/cart/count/

Should return JSON data.

---

## Common Django Errors

### Error: "No such table: store_cartitem"
**Solution:**
```bash
python manage.py migrate
```

### Error: "CSRF token missing or incorrect"
**Solution:**
1. Clear browser cookies
2. Add to settings.py:
```python
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
```

### Error: "Session key is None"
**Solution:**
Add to settings.py:
```python
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_SAVE_EVERY_REQUEST = True
```

---

## Debugging Steps

### 1. Check Server Logs
Look at terminal where `runserver` is running for error messages.

### 2. Enable Django Debug Toolbar
```bash
pip install django-debug-toolbar
```

Add to settings.py:
```python
INSTALLED_APPS = [
    ...
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    ...
]

INTERNAL_IPS = ['127.0.0.1']
```

### 3. Test with curl
```bash
# Test add to cart
curl -X POST http://127.0.0.1:8000/cart/add/1/ \
  -H "Content-Type: application/json" \
  -b cookies.txt -c cookies.txt
```

### 4. Check Database
```bash
python manage.py dbshell
```
```sql
SELECT * FROM store_cart;
SELECT * FROM store_cartitem;
SELECT * FROM store_order;
```

---

## Reset Everything (Nuclear Option)

If nothing works, reset the database:

```bash
# Backup first!
cp db.sqlite3 db.sqlite3.backup

# Delete database
del db.sqlite3  # Windows
# rm db.sqlite3  # Linux/Mac

# Recreate
python manage.py migrate
python manage.py createsuperuser
python manage.py populate_products

# Test again
python manage.py runserver
```

---

## Still Not Working?

1. **Check Python version**: Should be 3.8+
   ```bash
   python --version
   ```

2. **Check Django version**: Should be 4.0+
   ```bash
   python -m django --version
   ```

3. **Reinstall dependencies**:
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```

4. **Check file permissions**: Ensure db.sqlite3 is writable

5. **Disable antivirus temporarily**: Sometimes blocks local server

---

## Getting Help

If issues persist:
1. Copy the exact error message
2. Check Django logs in terminal
3. Check browser console (F12)
4. Share error details for specific help

---

## Prevention Tips

1. **Always run migrations** after model changes
2. **Clear browser cache** when testing
3. **Use incognito mode** for clean testing
4. **Check console** for JavaScript errors
5. **Keep Django updated**: `pip install --upgrade django`
