from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, UserManager

# Create your models here.
class neighborhood(models.Model):
    name = models.CharField(max_length=50, default = 'Nyaorofi')
    location = models.CharField(max_length=50, default='Nyairofi')
    occupants = models.ForeignKey("User.Model", on_delete=models.CASCADE)
    admin = models.ForeignKey("UserManager.Model", on_delete=models.CASCADE)
    
    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()
