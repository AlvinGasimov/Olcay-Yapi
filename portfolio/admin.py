from django.contrib import admin
from .models import *

class PortfolioImagesInline(admin.TabularInline):
    model = PortfolioImages
    extra = 1
    

@admin.register(Portfolio) 
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'slug']
    inlines = [PortfolioImagesInline]