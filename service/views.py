from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from main.forms import *
from django.contrib import messages

def services(request):
    services = Service.objects.all()
    
    context = {
        'services': services
    }
    
    return render(request, 'services.html', context)


def service_detail(request, service_slug):
    
    services = Service.objects.all()
    service = get_object_or_404(Service, slug=service_slug)
    images = ServiceImages.objects.filter(service=service)
    current_slug = service.slug
    
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Uğurla abunə olundu!!!")
            return redirect('main:index')
    else:
        form = SubscribeForm()
    
    context = {
        'service': service,
        'images': images,
        'current_slug' : current_slug,
        'services' : services
    }
    return render(request, 'service-details.html', context)