from django.db import models

class Contact(models.Model):
    ARCHITECT_STATUS_CHOICES = [
        ('yes', 'Memarsınız'),
        ('no', 'Memar deyilsiniz')
    ]
    
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    architect_status = models.CharField(max_length=3, choices=ARCHITECT_STATUS_CHOICES)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.email}"
