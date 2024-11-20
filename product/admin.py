from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(ProductCategory)
class ProductCategoryAdmin(TranslationAdmin):
    list_display = ('name', 'image', 'slug')
    group_fieldsets = True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(ProductBrand)
class ProductBrandAdmin(TranslationAdmin):
    list_display = ('name', 'image', 'slug')
    group_fieldsets = True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1
    

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'price', 'image', 'code', 'category', 'brand')
    inlines = [ProductImagesInline]
    group_fieldsets = True
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }