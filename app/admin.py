from django.contrib import admin
from .models import Category, Product, Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'active']
    list_filter = ['active']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'brand', 'price', 'publish', 'is_discount']
    list_filter = ['category', 'brand', 'publish', 'is_discount']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'Product']
    list_filter = ['id','Product']