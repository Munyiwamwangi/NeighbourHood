from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, UserManager

# Create your models here.
class neighborhood(models.Model):
    name = models.CharField(max_length=50, default = 'Nyaorofi')
    location = models.CharField(max_length=50, default='Nyairofi')
    occupants = models.ForeignKey("User.Model", on_delete=models.CASCADE)
    admin = models.ForeignKey("UserManager.Model", on_delete=models.CASCADE)
    
    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()
        
    def find_hoodbyname(cls, search_name):
        hood = cls.objects.filter(title__icontains=search_name)
        return hood

    class Meta:
        ordering = ['-id']
