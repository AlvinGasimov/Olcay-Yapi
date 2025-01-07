from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('references/', references, name='references'),
    path("set_language/<str:language>", set_language, name="set-language"),
]