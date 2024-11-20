from .models import *
from modeltranslation.translator import TranslationOptions,register


@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ('title','description', )


