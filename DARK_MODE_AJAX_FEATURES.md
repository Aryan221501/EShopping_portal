# Dark Mode & AJAX Features

## What's New

### 🌙 Dark Mode UI
- Modern dark theme with GitHub-inspired color scheme
- Smooth hover effects and transitions on product cards
- Bootstrap Icons integration for better visual appeal
- Responsive design that works on all devices
- Professional color palette optimized for readability

### ⚡ AJAX Features
1. **Live Search Suggestions**
   - Real-time search results as you type
   - Dropdown with product previews
   - No page reload required

2. **Dynamic Product Loading**
   - "Load More" button for infinite scroll
   - Products load via AJAX without page refresh
   - Smooth loading animations

3. **Category Filtering**
   - Filter products by category dynamically
   - Instant filtering without page reload

4. **AI Recommendations**
   - Recommendations load via AJAX on product detail page
   - Sidebar widget with top 3 similar products
   - Cached for performance

### 📦 Product Database
- **47 products** across 7 categories:
  - Electronics (7 products)
  - Fashion (7 products)
  - Home & Kitchen (7 products)
  - Books (6 products)
  - Sports (7 products)
  - Beauty (6 products)
  - Toys (7 products)

## API Endpoints

New AJAX endpoints added:
- `/api/search/?q=query` - Live search suggestions
- `/api/products/?page=1` - Paginated products
- `/api/categories/` - List all categories
- `/api/recommend/<id>/` - Get recommendations for a product

## How to Run

1. Activate virtual environment:
   ```
   venv\Scripts\activate
   ```

2. Run the development server:
   ```
   python manage.py runserver
   ```

3. Open http://127.0.0.1:8000/

## Features Showcase

### Home Page
- Grid layout with product cards
- Category filter dropdown
- Load more button for pagination
- Hover effects on cards

### Product Detail Page
- Large product display
- AI recommendations sidebar (AJAX loaded)
- Add to cart button with animation
- Related products section

### Search Page
- Live search suggestions in navbar
- Full search results page
- Product count display

### Responsive Design
- Mobile-friendly navigation
- Collapsible navbar on small screens
- Responsive grid (4 columns → 3 → 2 → 1)

## Technical Details

### Dark Mode Colors
- Primary Background: `#0d1117`
- Secondary Background: `#161b22`
- Tertiary Background: `#21262d`
- Accent Color: `#58a6ff`
- Text Primary: `#c9d1d9`
- Text Secondary: `#8b949e`

### Performance
- Recommendation caching (5 minutes)
- Paginated product loading (24 per page)
- Optimized database queries
- Minimal JavaScript for fast loading
