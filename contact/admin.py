from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Contact)
class ContactAdmin(TranslationAdmin):
    list_display = ('username', 'email', 'phone', 'architect_status')
    
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
        
        
        
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'country', 'phone')