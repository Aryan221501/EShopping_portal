# AI-Powered E-Shop

A modern e-commerce platform with integrated AI features including chatbots, product recommendations, and semantic search capabilities.

## 🌟 Features

- **Dark Theme UI**: Modern GitHub-inspired interface with smooth animations
- **Complete E-Commerce**: Shopping cart, checkout, orders, and product management
- **AI Chatbot**: 24/7 customer support with natural language processing
- **Smart Recommendations**: TF-IDF and sentence embedding-based product suggestions
- **Real-time Trends**: Trending products analysis based on user behavior
- **Dynamic Interactions**: AJAX-powered seamless browsing experience
- **Responsive Design**: Works on all devices

## 🛠️ Tech Stack

- **Backend**: Django 4.2+
- **Database**: SQLite (production-ready with PostgreSQL upgrade path)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5.3, AJAX
- **AI Components**: Transformers, PyTorch, Sentence Transformers, Scikit-learn

## 🚀 Quick Start

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai_eshop_project
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   python manage.py populate_products
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`

## 🤖 AI Features Setup

To enable advanced AI features:

1. Install additional AI dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. The AI models will download automatically on first use

3. For enhanced AI with Google's Gemini API, set the environment variable:
   ```bash
   export GEMINI_API_KEY='your-api-key-here'
   ```

## 📁 Project Structure

```
ai_eshop_project/
├── eshop/                  # Django project settings
├── store/                  # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # Application logic
│   ├── ai_services.py      # AI integration
│   ├── gemini_service.py   # Google Gemini integration
│   └── urls.py             # URL routing
├── templates/              # HTML templates
├── static/                 # Static files (CSS, JS, Images)
├── manage.py               # Django management commands
└── requirements.txt        # Python dependencies
```

## 📝 Documentation

For comprehensive documentation, check out these files in the repository:
- `AI_FEATURES_GUIDE.md` - Complete AI technical guide
- `QUICK_START.md` - Get running in 5 minutes
- `TROUBLESHOOTING.md` - Fix common issues
- `DEBUG_INSTRUCTIONS.md` - Debugging guide

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

If you encounter any issues, please check the documentation files in the project directory or open an issue on GitHub.