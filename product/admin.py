from django.contrib import admin
from .models import *
    

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'slug')


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'slug')


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'code', 'category', 'brand')
    inlines = [ProductImagesInline]