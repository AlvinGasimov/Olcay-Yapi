from .models import *
from modeltranslation.translator import TranslationOptions,register


@register(Contact)
class NavigationItemTranslationOptions(TranslationOptions):
    fields = ('architect_status','message',)