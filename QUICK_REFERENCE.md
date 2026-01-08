# 🚀 Quick Reference Card

## Installation & Setup

```bash
# Basic setup (no AI)
cd ai_eshop_project
python manage.py migrate
python manage.py populate_products
python manage.py runserver

# With AI features
install_ai.bat  # Windows (or pip install -r requirements.txt)
python manage.py runserver
```

## URLs

| Feature | URL |
|---------|-----|
| Home | http://127.0.0.1:8000/ |
| AI Chatbot | http://127.0.0.1:8000/chatbot/ |
| Trending | http://127.0.0.1:8000/trending/ |
| Cart | http://127.0.0.1:8000/cart/ |
| Checkout | http://127.0.0.1:8000/checkout/ |
| Admin | http://127.0.0.1:8000/admin/ |

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/chatbot/` | POST | Chat with AI |
| `/api/recommend-advanced/<id>/` | GET | AI recommendations |
| `/api/search/` | GET | Live search |
| `/api/products/` | GET | Paginated products |
| `/api/categories/` | GET | Category list |
| `/api/cart/count/` | GET | Cart item count |

## Chatbot Queries

```
"Find wireless headphones"
"What's your shipping policy?"
"Show me products under 2000"
"How do I track my order?"
"Recommend products for fitness"
```

## File Structure

```
ai_eshop_project/
├── store/
│   ├── ai_services.py      # 🤖 AI engine
│   ├── views.py            # Views + APIs
│   ├── models.py           # Database models
│   └── urls.py             # URL routing
├── templates/store/
│   ├── chatbot.html        # 🤖 Chatbot UI
│   ├── trending.html       # 🔥 Trending
│   ├── cart.html           # 🛒 Cart
│   └── checkout.html       # 💳 Checkout
└── static/css/
    └── dark-theme.css      # 🎨 Dark mode
```

## Commands

```bash
# Migrations
python manage.py makemigrations
python manage.py migrate

# Create products
python manage.py populate_products

# Admin user
python manage.py createsuperuser

# Run server
python manage.py runserver

# Test AI
python manage.py shell < test_ai_features.py

# Test cart
python manage.py shell < test_cart.py
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Cart not working | `python manage.py migrate` + clear browser cache |
| AI models not downloading | Check internet, manually download |
| Out of memory | Use TF-IDF only (edit ai_services.py) |
| Slow recommendations | Limit products analyzed |
| CSRF errors | Clear cookies, restart server |

## Configuration

### Chatbot Intents
Edit `store/ai_services.py` line ~50

### Recommendation Weights
Edit `store/ai_services.py` line ~200

### Trending Period
Edit `store/ai_services.py` line ~180

## Documentation

| File | Purpose |
|------|---------|
| AI_README.md | AI quick start |
| AI_FEATURES_GUIDE.md | Complete AI guide |
| AI_INTEGRATION_IDEAS.md | Future features |
| QUICK_START.md | 5-minute setup |
| TROUBLESHOOTING.md | Fix issues |
| FINAL_SUMMARY.md | Complete summary |

## Performance

- Page load: <1s
- AJAX: <500ms
- AI chatbot: <500ms
- Recommendations: <1s (cached)
- Memory: ~1.5GB with AI

## Features Checklist

✅ Dark mode UI
✅ AJAX interactions
✅ Shopping cart
✅ Checkout
✅ AI chatbot
✅ Advanced recommendations
✅ Trending products
✅ 47 sample products
✅ Admin panel
✅ API endpoints

## Cost

**FREE!**
- No API keys
- No monthly fees
- Open-source models
- Self-hosted

## Next Steps

1. Install AI: `install_ai.bat`
2. Test chatbot: `/chatbot/`
3. Check recommendations
4. View trending: `/trending/`
5. Customize & deploy!

---

**Need help?** Check TROUBLESHOOTING.md or AI_FEATURES_GUIDE.md
