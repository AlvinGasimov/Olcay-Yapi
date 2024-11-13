from django.urls import path
from .views import *

app_name = 'portfolio'

urlpatterns = [
    path('', portfolios, name='portfolios'),
    path('<slug:portfolio_slug>', portfolio_detail, name='portfolio_detail')
]