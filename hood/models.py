from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, UserManager

# Create your models here.


class Neighborhood(models.Model):
    hood_image = models.ImageField(upload_to='images/',  blank=True)
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
        
    @classmethod
    def search_by_hood_name(cls, search_term):
        hood = cls.objects.filter(hood_name__icontains=search_term)
        return hood
    class Meta:
        ordering = ['-id']


class Neighbor(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=20)
    contact = models.CharField(max_length=12)
    profile_picture = models.ImageField(upload_to='images/', default = 'profdefault.jpg')
    bio = models.CharField(max_length=70)
    neighborhood = models.ForeignKey(
        Neighborhood, on_delete=models.CASCADE, null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    class Meta:
        ordering = ['-id']

    def update_bio(self, bio):
        self.bio = bio
        self.save()

    def __str__(self):
        return f'{Neighbor}'

class Post(models.Model):
    writer = models.ManyToManyField(User, null=True)
    title = models.CharField(max_length=70)
    contact = models.OneToOneField(Neighbor, on_delete=models.CASCADE)
    description = models.TextField(max_length=300, default=0)
    post_writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    neighbourhood = models.ForeignKey(
        Neighborhood, on_delete=models.CASCADE, null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    class Meta:
        ordering = ['-id']


class Business(models.Model):
    business_name = models.CharField(max_length = 20)
    business_email = models.CharField(max_length = 20)
    description = models.TextField(max_length=300,default=0)
    contact = models.CharField(max_length=12)
    business_image = models.ImageField(upload_to = 'images/',blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    business_hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)


    def create_business(self):
        self.create()

    def delete_business(self):
        self.delete()

    def update_business(self,business):
        self.business = business
        self.update()
