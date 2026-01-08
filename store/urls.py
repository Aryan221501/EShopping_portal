from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('recommend/<int:pk>/', views.recommend, name='recommend'),
    
    # Cart and Checkout
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:pk>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/<str:order_number>/', views.order_confirmation, name='order_confirmation'),
    
    # AI Features
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('trending/', views.trending_products, name='trending'),
    path('ai-recommend/<int:pk>/', views.ai_recommend_advanced, name='ai_recommend_advanced'),
    
    # API endpoints for AJAX
    path('api/search/', views.api_search, name='api_search'),
    path('api/products/', views.api_products, name='api_products'),
    path('api/categories/', views.api_categories, name='api_categories'),
    path('api/recommend/<int:pk>/', views.api_recommend, name='api_recommend'),
    path('api/recommend-advanced/<int:pk>/', views.api_recommend_advanced, name='api_recommend_advanced'),
    path('api/cart/count/', views.get_cart_count, name='get_cart_count'),
    path('api/chatbot/', views.chatbot_api, name='chatbot_api'),
]
