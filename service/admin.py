from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
class ServiceImagesInline(admin.TabularInline):
    model = ServiceImages
    extra = 1
  

class ServiceMainImageInline(admin.TabularInline):
    model = ServiceMainImage
    extra = 1
    
    
class ServiceVideoInline(admin.TabularInline):
    model = ServiceVideo
    extra = 1
    
    
@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('name', 'image', 'icon')
    inlines = [ServiceMainImageInline, ServiceImagesInline, ServiceVideoInline]
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