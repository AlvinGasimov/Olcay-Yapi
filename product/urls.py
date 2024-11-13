from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('', products, name='products'),
    path('categories/', categories, name='categories'),
    path('<slug:product_slug>/', product_detail, name='product_detail'),
    path('brands', brands, name='brands')
]