# 🚀 Quick Start Guide

## Get Your E-Shop Running in 5 Minutes!

### Step 1: Open Terminal
```bash
cd ai_eshop_project
```

### Step 2: Apply Database Migrations
```bash
python manage.py migrate
```
Expected output: `Operations to perform: Apply all migrations...`

### Step 3: Create Sample Products (47 products)
```bash
python manage.py populate_products
```
Expected output: `Successfully created 47 products!`

### Step 4: Start the Server
```bash
python manage.py runserver
```
Expected output: `Starting development server at http://127.0.0.1:8000/`

### Step 5: Open in Browser
```
http://127.0.0.1:8000/
```

**That's it! Your dark mode e-shop is running! 🎉**

---

## 🎯 Quick Test

1. **Browse products** on homepage
2. **Click any product** to view details
3. **Click "Add to Cart"** - watch the cart badge update!
4. **Click "Cart"** in navbar - see your items
5. **Click "Proceed to Checkout"**
6. **Fill the form** and click "Place Order"
7. **See order confirmation** with order number

---

## 🛠️ Optional: Create Admin Account

```bash
python manage.py createsuperuser
```

Then visit: http://127.0.0.1:8000/admin/

---

## ❓ Having Issues?

### Cart not working?
```bash
# Clear browser cache (Ctrl+Shift+Delete)
# Then refresh page (Ctrl+F5)
```

### Still not working?
See **DEBUG_INSTRUCTIONS.md** for detailed troubleshooting.

---

## 📚 What to Read Next

1. **SUMMARY.md** - Overview of all features
2. **AI_INTEGRATION_IDEAS.md** - How to add AI features
3. **DARK_MODE_AJAX_FEATURES.md** - Feature documentation
4. **TROUBLESHOOTING.md** - Fix common issues

---

## 🎨 Features You'll See

✅ Dark mode UI
✅ Live search suggestions
✅ Product filtering
✅ Shopping cart
✅ Checkout system
✅ Order confirmation
✅ AI recommendations
✅ 47 sample products

---

## 🚀 Next Steps

1. **Explore the site** - Add products to cart, checkout
2. **Check admin panel** - Manage products, orders
3. **Read AI_INTEGRATION_IDEAS.md** - Plan AI features
4. **Customize** - Change colors, add features

---

**Enjoy your AI-powered e-shop! 🛍️**
