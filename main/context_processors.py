from .models import *
from portfolio.models import *
from product.models import *
from service.models import *

def site_settings(request):
    navigation_item = NavigationItem.objects.first()
    about = About.objects.first()
    mission = Mission.objects.first()
    vision = Vision.objects.first()
    statistic = Statistic.objects.first()
    faq = FAQ.objects.first()
    partners = Partners.objects.all()
    works = Works.objects.all()[:3]
    product_categories = ProductCategory.objects.all()
    first_12_products = Product.objects.all()[:12]
    last_8_portfolios = Portfolio.objects.all().order_by('-created_at')[:8]
    services = Service.objects.all()
    last_6_services = Service.objects.all().order_by('-created_at')[:6]
    ceo = CEO.objects.last()
    
    context = {
        'navigation_item' : navigation_item,
        'about' : about,
        'mission' : mission,
        'vision' : vision,
        'statistic' : statistic,
        'faq' : faq,
        'partners' : partners,
        'works' : works,
        'product_categories' : product_categories,
        'first_12_products' : first_12_products,
        'last_8_portfolios' : last_8_portfolios,
        'services' : services,
        'last_6_services' : last_6_services,
        'ceo': ceo
    }
    return context