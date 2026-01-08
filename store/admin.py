from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Order, OrderItem, BehaviorLog

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'description']

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'session_key', 'user', 'created_at', 'get_item_count']
    inlines = [CartItemInline]

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'product_title', 'product_price', 'quantity']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'email', 'total_amount', 'status', 'placed_at']
    list_filter = ['status', 'placed_at']
    search_fields = ['order_number', 'full_name', 'email']
    readonly_fields = ['order_number', 'placed_at']
    inlines = [OrderItemInline]

@admin.register(BehaviorLog)
class BehaviorLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'event', 'timestamp']
    list_filter = ['event', 'timestamp']
