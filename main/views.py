from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

def index(request):
    home_items = Home.objects.all()
    statistic_slogans = Statistic.objects.all()
    
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Uğurla abunə olundu!!!")
            return redirect('main:index')
    else:
        form = SubscribeForm()
    
    context = {
        'home_items': home_items,
        'form' : form,
        'statistic_slogans' : statistic_slogans
    }
    
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')