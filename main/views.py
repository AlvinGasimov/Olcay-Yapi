from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from service.models import *
from portfolio.models import *
from product.models import *
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.core.paginator import Paginator

def index(request):
    home_items = Home.objects.all()
    statistic_slogans = Statistic.objects.all()
    video_slider = Slider.objects.order_by('-created_at').first()
    
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
        'statistic_slogans' : statistic_slogans,
        'video_slider' : video_slider
    }
    
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def references(request):
    references = Reference.objects.all().order_by('-created_at')
    paginator = Paginator(references, 60)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'references' : references
    }
    return render(request, 'references.html', context)



def set_language(request, language):
    if language not in dict(settings.LANGUAGES):
        return HttpResponseRedirect("/")

    referer = request.META.get("HTTP_REFERER", "/")
    try:
        view = resolve(urlparse(referer).path)
        translation.activate(language)
        app_name = view.app_name if hasattr(view, 'app_name') else None
        view_name = f"{app_name}:{view.url_name}" if app_name else view.url_name

        response = HttpResponseRedirect(
            reverse(view_name, args=view.args, kwargs=view.kwargs)
        )
    except Resolver404:
        response = HttpResponseRedirect("/")
    
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response