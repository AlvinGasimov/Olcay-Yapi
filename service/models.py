from django.db import models
from django.utils.text import slugify

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=255)
    image = models.ImageField(upload_to='service_images/')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name or "Unnamed Service"

    class Meta:
        verbose_name_plural = 'Xidmətlər'


class ServiceImages(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='service_images/')

    def __str__(self):
        return f"Image for {self.service.name or 'Unnamed Service'}"

    class Meta:
        verbose_name_plural = 'Xidmət şəkilləri'


class ServiceMainImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='main_images')
    image = models.ImageField(upload_to='service_main_images/', null=True, blank=True)

    def __str__(self):
        return f"Main image for {self.service.name or 'Unnamed Service'}"

    class Meta:
        verbose_name_plural = 'Xidmətin əsas şəkiləri'


class ServiceVideo(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='videos')
    video = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Video for {self.service.name or 'Unnamed Service'}"

    class Meta:
        verbose_name_plural = 'Xidmət videoları'