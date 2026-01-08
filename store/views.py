from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.cache import cache
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Product, Category, Cart, CartItem, Order, OrderItem, BehaviorLog
from collections import Counter
import math
def home(request):
    products = Product.objects.all()[:24]
    return render(request, 'store/home.html', {'products': products})
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # log behavior (simple)
    if request.user.is_authenticated:
        from .models import BehaviorLog
        BehaviorLog.objects.create(user=request.user, product=product, event='view')
    return render(request, 'store/product_detail.html', {'product': product})
def tokenize(text):
    return [t.lower() for t in text.split() if t.isalnum() or t.isalpha() or t.isdigit()]
def score_similarity(a, b):
    # simple token-overlap cosine-like score
    ca = Counter(tokenize(a))
    cb = Counter(tokenize(b))
    common = set(ca.keys()) & set(cb.keys())
    num = sum(ca[k]*cb[k] for k in common)
    denom = math.sqrt(sum(v*v for v in ca.values())) * math.sqrt(sum(v*v for v in cb.values()))
    return num/denom if denom else 0.0
def recommend(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cache_key = f"rec_{pk}"
    recs = cache.get(cache_key)
    if recs is None:
        candidates = Product.objects.exclude(pk=pk)[:200]
        scored = []
        for c in candidates:
            s = score_similarity(product.title + ' ' + product.description, c.title + ' ' + c.description)
            if s>0:
                scored.append((s, c))
        scored.sort(key=lambda x: -x[0])
        recs = [p.id for _s,p in scored[:10]]
        cache.set(cache_key, recs, 60*5)  # cache 5 minutes
    products = Product.objects.filter(id__in=recs)
    return render(request, 'store/recommend.html', {'products': products, 'base': product})
def search(request):
    q = request.GET.get('q','').strip()
    products = []
    if q:
        # token-match search + simple ranking by matches
        parts = q.lower().split()
        qs = Product.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))[:200]
        scored = []
        for p in qs:
            text = (p.title + ' ' + p.description).lower()
            score = sum(text.count(part) for part in parts)
            scored.append((score, p))
        scored.sort(key=lambda x: -x[0])
        products = [p for s,p in scored if s>0]
    return render(request, 'store/search.html', {'products': products, 'q': q})


# API endpoints for AJAX
def api_search(request):
    q = request.GET.get('q', '').strip()
    products = []
    if q and len(q) >= 2:
        parts = q.lower().split()
        qs = Product.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))[:10]
        products = [{
            'id': p.id,
            'title': p.title,
            'description': p.description,
            'price': str(p.price),
            'category': p.category.name
        } for p in qs]
    return JsonResponse({'products': products})

def api_products(request):
    page = int(request.GET.get('page', 1))
    products_list = Product.objects.all().order_by('-created_at')
    paginator = Paginator(products_list, 24)
    page_obj = paginator.get_page(page)
    
    products = [{
        'id': p.id,
        'title': p.title,
        'description': p.description,
        'price': str(p.price),
        'category_name': p.category.name,
        'category_slug': p.category.slug
    } for p in page_obj]
    
    return JsonResponse({
        'products': products,
        'has_more': page_obj.has_next()
    })

def api_categories(request):
    categories = Category.objects.all()
    return JsonResponse({
        'categories': [{'name': c.name, 'slug': c.slug} for c in categories]
    })

def api_recommend(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cache_key = f"rec_{pk}"
    recs = cache.get(cache_key)
    if recs is None:
        candidates = Product.objects.exclude(pk=pk)[:200]
        scored = []
        for c in candidates:
            s = score_similarity(product.title + ' ' + product.description, c.title + ' ' + c.description)
            if s > 0:
                scored.append((s, c))
        scored.sort(key=lambda x: -x[0])
        recs = [p.id for _s, p in scored[:10]]
        cache.set(cache_key, recs, 60*5)
    
    products = Product.objects.filter(id__in=recs)
    return JsonResponse({
        'products': [{
            'id': p.id,
            'title': p.title,
            'description': p.description,
            'price': str(p.price),
            'category': p.category.name
        } for p in products]
    })


# Cart and Checkout Views
def get_or_create_cart(request):
    """Get or create cart for session"""
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    
    cart, created = Cart.objects.get_or_create(
        session_key=session_key,
        defaults={'user': request.user if request.user.is_authenticated else None}
    )
    return cart

def cart_view(request):
    cart = get_or_create_cart(request)
    cart_items = cart.items.all()
    return render(request, 'store/cart.html', {
        'cart': cart,
        'cart_items': cart_items
    })

def add_to_cart(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        cart = get_or_create_cart(request)
        
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': 1}
        )
        
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        # Log behavior
        if request.user.is_authenticated:
            BehaviorLog.objects.create(user=request.user, product=product, event='add_to_cart')
        
        return JsonResponse({
            'success': True,
            'cart_count': cart.get_item_count(),
            'message': f'{product.title} added to cart'
        })
    return JsonResponse({'success': False}, status=400)

def update_cart_item(request, pk):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, pk=pk)
        action = request.POST.get('action')
        
        if action == 'increase':
            cart_item.quantity += 1
            cart_item.save()
        elif action == 'decrease':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
                return JsonResponse({
                    'success': True,
                    'deleted': True,
                    'cart_total': cart_item.cart.get_total(),
                    'cart_count': cart_item.cart.get_item_count()
                })
        
        return JsonResponse({
            'success': True,
            'quantity': cart_item.quantity,
            'subtotal': float(cart_item.get_subtotal()),
            'cart_total': float(cart_item.cart.get_total()),
            'cart_count': cart_item.cart.get_item_count()
        })
    return JsonResponse({'success': False}, status=400)

def remove_from_cart(request, pk):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, pk=pk)
        cart = cart_item.cart
        cart_item.delete()
        
        return JsonResponse({
            'success': True,
            'cart_total': float(cart.get_total()),
            'cart_count': cart.get_item_count()
        })
    return JsonResponse({'success': False}, status=400)

def checkout(request):
    cart = get_or_create_cart(request)
    
    if not cart.items.exists():
        return redirect('cart')
    
    if request.method == 'POST':
        # Create order
        import uuid
        order_number = f"ORD-{uuid.uuid4().hex[:8].upper()}"
        
        order = Order.objects.create(
            order_number=order_number,
            user=request.user if request.user.is_authenticated else None,
            session_key=request.session.session_key,
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            postal_code=request.POST.get('postal_code'),
            total_amount=cart.get_total()
        )
        
        # Create order items
        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                product_title=cart_item.product.title,
                product_price=cart_item.product.price,
                quantity=cart_item.quantity
            )
        
        # Clear cart
        cart.items.all().delete()
        
        return redirect('order_confirmation', order_number=order.order_number)
    
    return render(request, 'store/checkout.html', {
        'cart': cart,
        'cart_items': cart.items.all()
    })

def order_confirmation(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, 'store/order_confirmation.html', {'order': order})

def get_cart_count(request):
    cart = get_or_create_cart(request)
    return JsonResponse({'count': cart.get_item_count()})


# AI Chatbot Views (optional - only if AI packages installed)
try:
    from .ai_services import chatbot_service, recommendation_service
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False
    chatbot_service = None
    recommendation_service = None

def chatbot_view(request):
    """Chatbot page"""
    if not AI_AVAILABLE:
        return render(request, 'store/chatbot_unavailable.html')
    return render(request, 'store/chatbot.html')

def chatbot_api(request):
    """API endpoint for chatbot - Now powered by Gemini AI!"""
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        message = data.get('message', '')
        session_id = request.session.session_key
        
        if not session_id:
            request.session.create()
            session_id = request.session.session_key
        
        # Try Gemini first, fallback to original chatbot
        try:
            from .gemini_service import gemini_chatbot
            response = gemini_chatbot.chat(message, session_id)
        except Exception as e:
            print(f"Gemini fallback: {e}")
            # Fallback to original chatbot
            if AI_AVAILABLE:
                response = chatbot_service.chat(message, session_id)
            else:
                response = {
                    'response': 'Hello! I can help you find products, answer questions about shipping and returns. What would you like to know?',
                    'intent': 'fallback',
                    'products': []
                }
        
        return JsonResponse(response)
    
    return JsonResponse({'error': 'POST required'}, status=400)

def ai_recommend_advanced(request, pk):
    """Advanced AI recommendations using TF-IDF and embeddings"""
    product = get_object_or_404(Product, pk=pk)
    
    if not AI_AVAILABLE:
        # Fallback to basic recommendations
        return redirect('recommend', pk=pk)
    
    user_id = request.user.id if request.user.is_authenticated else None
    
    # Get hybrid recommendations
    recommended_ids = recommendation_service.get_hybrid_recommendations(
        product_id=pk,
        user_id=user_id,
        limit=10
    )
    
    products = Product.objects.filter(id__in=recommended_ids)
    
    # Preserve order from recommendation
    products_dict = {p.id: p for p in products}
    ordered_products = [products_dict[pid] for pid in recommended_ids if pid in products_dict]
    
    return render(request, 'store/recommend.html', {
        'products': ordered_products,
        'base': product
    })

def trending_products(request):
    """Show trending products"""
    if not AI_AVAILABLE:
        # Fallback to newest products
        products = Product.objects.all().order_by('-created_at')[:20]
        return render(request, 'store/trending.html', {'products': products})
    
    trending_ids = recommendation_service.get_trending_products(limit=20)
    products = Product.objects.filter(id__in=trending_ids)
    
    # Preserve order
    products_dict = {p.id: p for p in products}
    ordered_products = [products_dict[pid] for pid in trending_ids if pid in products_dict]
    
    return render(request, 'store/trending.html', {'products': ordered_products})

def api_recommend_advanced(request, pk):
    """API for advanced recommendations"""
    if not AI_AVAILABLE:
        # Fallback to basic API
        return api_recommend(request, pk)
    
    user_id = request.user.id if request.user.is_authenticated else None
    
    recommended_ids = recommendation_service.get_hybrid_recommendations(
        product_id=pk,
        user_id=user_id,
        limit=10
    )
    
    products = Product.objects.filter(id__in=recommended_ids)
    products_dict = {p.id: p for p in products}
    ordered_products = [products_dict[pid] for pid in recommended_ids if pid in products_dict]
    
    return JsonResponse({
        'products': [{
            'id': p.id,
            'title': p.title,
            'description': p.description,
            'price': str(p.price),
            'category': p.category.name
        } for p in ordered_products]
    })
