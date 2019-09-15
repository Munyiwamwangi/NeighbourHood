from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User, UserManager

# Create your models here.


class Neighboorhood(models.Model):
    hood_image = models.ImageField(upload_to='images/',  blank=True)
    hood_name = models.CharField(max_length=20)
    hood_location = models.CharField(max_length=20)
    hood_occupants = models.IntegerField(default=0)
    neighbor = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.hood_location
    
    def save_hood(self):
        self.save()
        
    def delete_hood(self):
        self.delete()
        
    @classmethod
    def search_by_hood_name(cls, search_term):
        hood = cls.objects.filter(hood_name__icontains=search_term)
        return hood
    class Meta:
        ordering = ['-id']


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-id']


class Business(models.Model):
    business_name = models.CharField(max_length = 20)
    business_email = models.CharField(max_length = 20)
    description = models.TextField(max_length=300,default=0)
    contact = models.CharField(max_length=12)
    business_image = models.ImageField(upload_to = 'images/',blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    business_hood = models.ForeignKey(
        Neighboorhood, on_delete=models.CASCADE, null=True)


    def create_business(self):
        self.create()

    def delete_business(self):
        self.delete()

    def update_business(self,business):
        self.business = business
        self.update()
