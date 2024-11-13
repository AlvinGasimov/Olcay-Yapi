from django.contrib import admin
from .models import *

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'architect_status')