# 🤖 Gemini AI Integration Guide

## Overview

Your chatbot is now powered by **Google's Gemini AI** for intelligent, context-aware conversations!

## Setup Instructions

### 1. Install Gemini SDK

```bash
pip install google-generativeai
```

### 2. Get API Key

1. Visit: https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy your API key

### 3. Set Environment Variable

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your-api-key-here"
```

**Windows (CMD):**
```cmd
set GEMINI_API_KEY=your-api-key-here
```

**Linux/Mac:**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

**Or add to `.env` file:**
```
GEMINI_API_KEY=your-api-key-here
```

### 4. Test the Chatbot

```bash
python manage.py runserver
```

Visit: http://localhost:8000/chatbot/

## Features

### ✅ Intelligent Responses
- Context-aware conversations
- Natural language understanding
- Product search integration
- Store policy knowledge

### ✅ Conversation Memory
- Remembers last 10 messages per session
- Maintains context across conversation
- Personalized responses

### ✅ Product Integration
- Automatically searches products
- Shows relevant items
- Provides product details

### ✅ Fallback System
- Falls back to original chatbot if Gemini unavailable
- Graceful error handling
- Always provides responses

## How It Works

```python
# User sends message
message = "Find wireless headphones under 5000"

# Gemini processes with context
context = """
- Store information
- Product catalog
- Conversation history
"""

# Gemini generates intelligent response
response = gemini.generate_content(context + message)

# Products are searched and attached
products = search_products("wireless headphones")

# Response sent to user with products
```

## API Usage

### Chat Endpoint
```
POST /api/chatbot/
{
  "message": "Hello, I need help finding a laptop"
}
```

### Response
```json
{
  "response": "I'd be happy to help you find a laptop! What's your budget and what will you use it for?",
  "intent": "gemini_ai",
  "products": []
}
```

## Configuration

### System Prompt
Located in `store/gemini_service.py`:

```python
system_prompt = """
You are a helpful AI shopping assistant...
- Store policies
- Product categories
- Response guidelines
"""
```

### Conversation History
- Stores last 10 messages per session
- Automatically managed
- Cleared on session end

### Caching
- Responses cached for 5 minutes
- Reduces API calls
- Improves performance

## Troubleshooting

### Gemini Not Working?

**1. Check API Key**
```python
import os
print(os.getenv('GEMINI_API_KEY'))
```

**2. Check Installation**
```bash
pip show google-generativeai
```

**3. Check Logs**
```
Look for "✓ Gemini AI model loaded" in console
```

### Fallback Behavior

If Gemini fails:
1. Tries original chatbot (DialoGPT)
2. Falls back to pattern matching
3. Always provides a response

## Cost & Limits

### Gemini Pro (Free Tier)
- 60 requests per minute
- Free up to certain usage
- Check: https://ai.google.dev/pricing

### Optimization
- Responses cached (5 min)
- Short conversation history (10 msgs)
- Concise system prompts

## Files

- `store/gemini_service.py` - Gemini integration
- `store/views.py` - Chatbot endpoint
- `templates/store/chatbot.html` - UI

## Testing

### Test Gemini
```python
from store.gemini_service import gemini_chatbot

response = gemini_chatbot.chat("Hello!", session_id="test")
print(response)
```

### Test Product Search
```python
response = gemini_chatbot.chat("Find laptops under 50000", session_id="test")
print(response['products'])
```

## Benefits

✅ **Intelligent** - Understands context and intent  
✅ **Natural** - Human-like conversations  
✅ **Integrated** - Searches products automatically  
✅ **Reliable** - Fallback system ensures uptime  
✅ **Fast** - Cached responses, optimized prompts  

## Summary

Your chatbot now uses **Gemini AI** for:
- Natural conversations
- Context awareness
- Product recommendations
- Intelligent responses

With automatic fallback to ensure it always works! 🚀
