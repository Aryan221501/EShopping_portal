# 🤖 Chatbot Troubleshooting Guide

## Common Issues & Solutions

### Issue 1: Chatbot shows "AI not available" page

**Cause:** AI packages not installed

**Solution:**
```bash
pip install torch transformers sentence-transformers scikit-learn numpy
```

Or use the installer:
```bash
.\install_ai.bat  # PowerShell
```

Then restart server:
```bash
python manage.py runserver
```

---

### Issue 2: Chatbot not responding / No response

**Check 1: Browser Console**
1. Press F12 to open Developer Tools
2. Go to Console tab
3. Look for errors (red text)

**Common errors:**
- `403 Forbidden` → CSRF issue (clear cookies)
- `500 Internal Server Error` → Check server logs
- `Network error` → Server not running

**Solution:**
```bash
# Clear browser cache and cookies
# Restart server
python manage.py runserver
```

**Check 2: Server Logs**
Look at terminal where `runserver` is running for Python errors.

---

### Issue 3: Chatbot gives generic responses

**This is normal!** The chatbot uses rule-based intent matching, not GPT.

**What it can do:**
- ✅ Search products: "Find wireless headphones"
- ✅ Answer FAQs: "What's your shipping policy?"
- ✅ Help with cart: "How do I checkout?"
- ✅ Provide info: "What payment methods?"

**What it cannot do:**
- ❌ Have deep conversations
- ❌ Understand complex queries
- ❌ Remember long conversation history
- ❌ Generate creative content

**To improve responses:**
Edit `store/ai_services.py` and add more intents/patterns.

---

### Issue 4: Product search not working

**Test manually:**
```bash
python manage.py shell
```

```python
from store.models import Product
from django.db.models import Q

# Search for products
query = "wireless"
products = Product.objects.filter(
    Q(title__icontains=query) | Q(description__icontains=query)
)
print(f"Found {products.count()} products")
for p in products[:5]:
    print(f"- {p.title}")
```

**If no products found:**
```bash
python manage.py populate_products
```

---

### Issue 5: Chatbot is slow

**Cause:** First message loads AI models

**Solution:** This is normal. First message takes 2-3 seconds, then it's fast.

**To speed up:**
1. Models are cached after first load
2. Use lighter models (already using smallest)
3. Increase server resources

---

### Issue 6: "CSRF token missing" error

**Solution:**
```bash
# Clear browser cookies
# Hard refresh (Ctrl+F5)
# Restart server
```

Or add to `settings.py`:
```python
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
```

---

## Testing Chatbot

### Test 1: Check if AI is available
```bash
python manage.py shell
```

```python
try:
    from store.ai_services import chatbot_service
    print("✅ AI available")
except ImportError as e:
    print(f"❌ AI not available: {e}")
```

### Test 2: Test chatbot directly
```bash
python manage.py shell < test_chatbot_simple.py
```

### Test 3: Test via browser
1. Open: http://127.0.0.1:8000/chatbot/
2. Type: "Hello"
3. Should get greeting response
4. Type: "Find headphones"
5. Should show products

### Test 4: Test API endpoint
```bash
curl -X POST http://127.0.0.1:8000/api/chatbot/ \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}' \
  -b cookies.txt -c cookies.txt
```

---

## Improving Chatbot Responses

### Add New Intents

Edit `store/ai_services.py` (line ~50):

```python
'custom_intent': {
    'patterns': ['keyword1', 'keyword2', 'phrase'],
    'responses': [
        'Response option 1',
        'Response option 2',
        'Response option 3'
    ]
}
```

### Add More Patterns to Existing Intents

```python
'shipping': {
    'patterns': [
        'shipping', 'delivery', 'when will', 'how long', 
        'tracking',  # existing
        'ship', 'deliver', 'arrive', 'receive'  # add these
    ],
    'responses': [...]
}
```

### Improve Product Search

Edit `store/ai_services.py` (line ~160):

```python
# Current stop words
stop_words = ['what', 'where', 'when', 'find', 'show', 'need', 'want']

# Add more
stop_words = ['what', 'where', 'when', 'find', 'show', 'need', 'want', 
              'looking', 'search', 'for', 'the', 'and', 'with', 'can', 'you']
```

---

## Expected Behavior

### Good Queries:
- "Find wireless headphones" → Shows headphone products
- "What's your shipping policy?" → Explains shipping
- "How do I checkout?" → Explains checkout process
- "Show me electronics" → Shows electronic products
- "Help" → Shows what chatbot can do

### Queries That Won't Work Well:
- "Tell me a joke" → Generic response
- "What's the weather?" → Generic response
- "Write me a poem" → Generic response
- Very long complex questions → May not understand

---

## Performance Expectations

- **First message:** 2-3 seconds (loading models)
- **Subsequent messages:** <500ms
- **Product search:** <1 second
- **Memory usage:** ~1.5GB with AI loaded

---

## Debugging Steps

1. **Check if server is running**
   ```bash
   # Should see: Starting development server at http://127.0.0.1:8000/
   ```

2. **Check if AI packages installed**
   ```bash
   pip list | grep -E "torch|transformers|sentence"
   ```

3. **Check browser console (F12)**
   - Look for JavaScript errors
   - Check Network tab for failed requests

4. **Check server logs**
   - Look for Python exceptions
   - Check for import errors

5. **Test chatbot directly**
   ```bash
   python manage.py shell < test_chatbot_simple.py
   ```

---

## Still Not Working?

### Collect Information:
1. What message did you send?
2. What response did you get (or no response)?
3. Any errors in browser console (F12)?
4. Any errors in server logs?
5. Did you install AI packages?

### Quick Fixes:
```bash
# Restart everything
# Stop server (Ctrl+C)
# Clear browser cache
# Restart server
python manage.py runserver

# Hard refresh browser (Ctrl+F5)
```

### Nuclear Option:
```bash
# Reinstall AI packages
pip uninstall torch transformers sentence-transformers scikit-learn numpy
pip install torch transformers sentence-transformers scikit-learn numpy

# Restart server
python manage.py runserver
```

---

## Alternative: Use Without AI

If AI features are causing issues, you can disable them:

1. Don't install AI packages
2. Chatbot will show "AI not available" page
3. All other features work normally
4. Basic recommendations still work

---

## Contact & Support

- Check `AI_FEATURES_GUIDE.md` for detailed info
- Check `TROUBLESHOOTING.md` for general issues
- Review code in `store/ai_services.py`
- Test with `test_chatbot_simple.py`

---

**Remember:** The chatbot is rule-based, not GPT. It's designed for:
- Product search
- FAQ answers
- Basic customer support

For advanced conversational AI, you'd need to integrate GPT-4 API (paid).
