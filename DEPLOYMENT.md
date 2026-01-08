# Deployment Guide

This guide explains how to deploy the AI E-Shop application to various platforms.

## Heroku Deployment

### Prerequisites
- Heroku CLI installed
- Heroku account

### Steps
1. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```

2. Set environment variables:
   ```bash
   heroku config:set DJANGO_SECRET_KEY='your-secret-key'
   heroku config:set DEBUG=False
   # If using gemini AI:
   # heroku config:set GEMINI_API_KEY='your-gemini-api-key'
   ```

3. Deploy:
   ```bash
   git push heroku main
   ```

4. Run migrations:
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py populate_products
   ```

## Manual Deployment

### On your own server

1. Clone the repository:
   ```bash
   git clone https://github.com/Aryan221501/EShopping_portal.git
   cd EShopping_portal
   ```

2. Set up virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set environment variables:
   ```bash
   export DJANGO_SECRET_KEY='your-secret-key'
   export DEBUG=False
   # Optionally for gemini AI:
   # export GEMINI_API_KEY='your-gemini-api-key'
   ```

4. Run migrations and collect static files:
   ```bash
   python manage.py migrate
   python manage.py populate_products
   python manage.py collectstatic --noinput
   ```

5. Start the server:
   ```bash
   gunicorn eshop.wsgi:application
   ```

## Docker Deployment (Optional)

If you want to containerize the application, create a Dockerfile (not included by default):
```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "eshop.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## Environment Variables

The application uses the following environment variables:

- `DJANGO_SECRET_KEY` (required): Django secret key for cryptographic signing
- `DEBUG` (optional): Set to False for production (default: True)
- `ALLOWED_HOSTS` (optional): Comma-separated list of allowed hosts (default: localhost,127.0.0.1)
- `DATABASE_URL` (optional): Database URL for production databases (defaults to SQLite)
- `GEMINI_API_KEY` (optional): Google Gemini API key for enhanced AI features

## Database

- For development: SQLite is used by default
- For production: PostgreSQL is recommended (add appropriate DATABASE_URL)

## Static Files

The application uses WhiteNoise for serving static files in production. Make sure to run `collectstatic` in production environments.