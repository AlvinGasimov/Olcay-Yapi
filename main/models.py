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
        verbose_name = 'Navigation Item'
        verbose_name_plural = 'Navigation Items'
        

class Home(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='home_images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
    

class Mission(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='mission_images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Mission'
        verbose_name_plural = 'Mission'
        

class Vision(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='vision_images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Vision'
        verbose_name_plural = 'Vision'
        
        
class Statistic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Statistic'
        verbose_name_plural = 'Statistic'
        

class StatisticSlogan(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    statistic = models.ForeignKey(Statistic, on_delete=models.CASCADE, related_name='slogans')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Statistic Slogan'
        verbose_name_plural = 'Statistic Slogan'


class FAQ(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='faq', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        
        
class QuestionAnswer(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE, related_name='question_answers')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Question Answer'
        verbose_name_plural = 'Question Answers'

class Works(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'
        
class Partners(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='partners_images/')
    url = models.URLField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'
        
        
class Subscribe(models.Model):
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribes'
        
        
