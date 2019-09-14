from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, UserManager

# Create your models here.


class Neighborhood(models.Model):
    hood_image = models.ImageField(upload_to='images/', blank=True)
    hood_name = models.CharField(max_length=20)
    hood_location = models.CharField(max_length=20)
    hood_occupants = models.IntegerField(default=0)
    neighbor = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.location
    
    def save_hood(self):
        self.save()
        
    def delete_hood(self):
        self.delete()
    class Meta:
        ordering = ['-id']

