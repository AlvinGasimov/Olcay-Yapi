from django.contrib import admin
from .models import *

@admin.register(NavigationItem)
class NavigationItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'phone_number', 'email', 'navbar_img', 'footer_img')
    
    
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    
    
@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    
    
@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    

class StatisticSloganInline(admin.TabularInline):
    model = StatisticSlogan
    extra = 1
    

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [StatisticSloganInline]
    
    
class QuestionAnswerInline(admin.TabularInline):
    model = QuestionAnswer
    extra = 1
    
    
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [QuestionAnswerInline]
    

@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')
    
@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'url')
    
admin.site.register(Subscribe)