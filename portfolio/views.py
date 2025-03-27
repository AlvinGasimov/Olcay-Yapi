from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import *
from main.forms import SubscribeForm
from django.contrib import messages

def portfolios(request):
    portfolios = Portfolio.objects.all()
    paginator = Paginator(portfolios, 16)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'portfolios.html', context)


def portfolio_detail(request, portfolio_slug):
    portfolios = Portfolio.objects.all()
    portfolio = get_object_or_404(Portfolio, slug = portfolio_slug)
    current_slug = portfolio.slug
    
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Uğurla abunə olundu!!!")
            return redirect('main:index')
    else:
        form = SubscribeForm()
    
    context = {
        'portfolios': portfolios,
        'portfolio': portfolio,
        'current_slug' : current_slug,
        'form' : form
    }
    return render(request, 'portfolio-details.html', context)