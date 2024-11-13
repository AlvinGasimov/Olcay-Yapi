from django.contrib import admin
from .models import *

class ProductImagesInline(admin.TabularInline):
    model = ServiceImages
    extra = 1
    
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'icon')
    inlines = [ProductImagesInline]