from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator

def products(request):
    category_filter = request.GET.get("category")
    brand_filter = request.GET.get("brand")
    products = Product.objects.all()
    search = request.GET.get('search', '')
    
    if search:
        products = products.filter(name__icontains=search)
    
    if category_filter:
        products = products.filter(category__slug=category_filter)
    
    if brand_filter:
        products = products.filter(brand__slug=brand_filter)
    
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    brands = ProductBrand.objects.all()

    context = {
        'page_obj': page_obj,
        'category_filter': category_filter,
        'brand_filter': brand_filter,
        'brands': brands,
    }
    
    return render(request, 'products.html', context)

def categories(request):
    
    categories = ProductCategory.objects.all()
    paginator = Paginator(categories, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'categories': categories,
        'page_obj' : page_obj
    }
    return render(request, 'products-category.html', context)
    

def product_detail(request, product_slug):
    products = Product.objects.all()
    product = get_object_or_404(Product, slug=product_slug)
    images = ProductImages.objects.filter(product=product)
    current_slug = product.slug
    same_products = Product.objects.filter(category=product.category).exclude(id=product.id)
    
    context = {
        'product': product,
        'images': images,
        'current_slug' : current_slug,
        'products' : products,
        "same_products" : same_products
    }
    
    return render(request, 'product-details.html', context)


def brands(request):
    brands = ProductBrand.objects.all()
    paginator = Paginator(brands, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'brands': brands,
        'page_obj': page_obj,
    }
    return render(request, 'markalar.html', context)