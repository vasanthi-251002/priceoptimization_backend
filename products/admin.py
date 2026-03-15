from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'cost_price', 'selling_price',
                    'stock_available', 'units_sold', 'optimized_price']
    list_filter = ['category']
    search_fields = ['name', 'description']
    ordering = ['-created_at']
