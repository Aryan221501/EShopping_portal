# AI E-Shop Project - Repository Structure

## Directory Structure
```
ai_eshop_project/                 # Root project directory
├── eshop/                       # Django project settings
│   ├── __init__.py
│   ├── settings.py              # Main settings (dev/prod ready)
│   ├── production_settings.py   # Production-specific settings
│   ├── urls.py                  # Main URL configuration
│   └── wsgi.py                  # WSGI application
├── store/                       # Main e-commerce app
│   ├── __init__.py
│   ├── admin.py                 # Admin interface configuration
│   ├── apps.py                  # App configuration
│   ├── models.py                # Database models
│   ├── views.py                 # View functions and controllers
│   ├── urls.py                  # Store URLs
│   ├── ai_services.py           # AI chatbot and recommendation services
│   └── gemini_service.py        # Google Gemini AI integration
├── templates/                   # HTML templates
│   ├── base.html               # Base layout template
│   └── store/                  # Store-specific templates
│       ├── home.html           # Home page
│       ├── product_detail.html # Product detail page
│       ├── cart.html           # Shopping cart
│       ├── checkout.html       # Checkout page
│       ├── chatbot.html        # AI chatbot interface
│       └── trending.html       # Trending products
├── static/                      # Static assets (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── .env.example                 # Example environment variables
├── .gitignore                   # Files to ignore in Git
├── DEPLOYMENT.md                # Deployment instructions
├── LICENSE                      # MIT License
├── ORIGINAL_README.md           # Original detailed README
├── README.md                    # GitHub-optimized README
├── Procfile                     # Process type declarations
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── db.sqlite3                   # Default database (will be recreated)
└── Various documentation files  # Additional docs for features
```

## Security Notes

### Protected Information
- API keys (like GEMINI_API_KEY) are only read from environment variables
- Secret keys are set via environment variables
- No sensitive data is hardcoded in the source code
- Credentials are referenced only in `.env.example` (not committed)

### Safe for Public Repository
- All actual credentials are stored in environment variables
- Sample data and models are included for demonstration
- Proper `.gitignore` prevents accidental commits of sensitive files
- Settings are configured to use environment variables for sensitive data

## Deployment Ready
- Production settings configuration included
- Proper static file handling for production
- Database configuration supports both dev (SQLite) and prod (PostgreSQL)
- Security settings enabled for production environments

## Development Ready
- Simple setup process with detailed documentation
- Sample data population scripts included
- Development settings optimized for ease of use
- Comprehensive documentation for all features