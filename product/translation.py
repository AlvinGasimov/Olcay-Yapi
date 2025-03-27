from .models import *
from modeltranslation.translator import TranslationOptions,register


@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    

@register(ProductBrand)
class ProductBrandTranslationOptions(TranslationOptions):
    fields = ('name',)
    

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
    
