from django.db import models

class NavigationItem(models.Model):
    title = models.CharField(max_length=100)
    navbar_img = models.ImageField(upload_to='navbar_images/')
    footer_img = models.ImageField(upload_to='footer_images/')
    address = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    facebook_link = models.URLField(max_length=400, null=True, blank=True)
    instagram_link = models.URLField(max_length=400, null=True, blank=True)
    whatsapp_link = models.URLField(max_length=400, null=True, blank=True)
    telegram_link = models.URLField(max_length=400, null=True, blank=True)
    twitter_link = models.URLField(max_length=400, null=True, blank=True)
    linkedin_link = models.URLField(max_length=400, null=True, blank=True)
    youtube_link = models.URLField(max_length=400, null=True, blank=True)
    map_link = models.URLField(max_length=400, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Navigation məlumatları'


class Home(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='home_images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Ana Səhifə'

class Slider(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='slider_videos/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Slider'


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Haqqımızda'
    

class Mission(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='mission_images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Misyonlar'
        

class Vision(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='vision_images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Vizyonlar'
        
        
class Statistic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Statistikalar'
        

class StatisticSlogan(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE, related_name='slogans')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Statistika Sloganları'


class FAQ(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='faq', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ-lar'
        
        
class QuestionAnswer(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE, related_name='question_answers')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Sual Cavablar'

class Works(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'İşlər'
        
class Partners(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='partners_images/')
    url = models.URLField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Partnyolrar'
        
        
class Subscribe(models.Model):
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Abunələr'
        
        
class CEO(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    keywords = models.CharField(max_length=200, null=True, blank=True)
    og_title = models.CharField(max_length=200, null=True, blank=True)
    og_description = models.TextField(null=True, blank=True)
    og_image = models.ImageField(upload_to='og_images/', null=True, blank=True)
    favicon = models.ImageField(upload_to='favicons/', null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ceo/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'CEO'
        verbose_name_plural = 'CEO-lar'
        
        
class Reference(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='reference')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Referanslar'