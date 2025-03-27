from .models import *
from modeltranslation.translator import TranslationOptions,register


@register(NavigationItem)
class NavigationItemTranslationOptions(TranslationOptions):
    fields = ('title','address', )


@register(Home)
class HomeTranslationOptions(TranslationOptions):
    fields = ('title','description', )


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title','description', )
    

@register(Mission)
class MissionTranslationOptions(TranslationOptions):
    fields = ('title','description', )
    


@register(Vision)
class VisionTranslationOptions(TranslationOptions):
    fields = ('title','description', )
    

@register(Statistic)
class StatisticTranslationOptions(TranslationOptions):
    fields = ('title','description', )
    

@register(StatisticSlogan)
class StatisticSloganTranslationOptions(TranslationOptions):
    fields = ('title', )
    


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(QuestionAnswer)
class QuestionAnswerTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)
    

@register(Works)
class WorksTranslationOptions(TranslationOptions):
    fields = ('title','description', )
  

@register(Partners)
class PartnersTranslationOptions(TranslationOptions):
    fields = ('title', )
  
  
@register(CEO)
class CEOTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords', 'og_title', 'og_description', 'author', 'position')