from django.contrib import admin
from .models import People,Business,Post,Neighboorhood

# Register your models here.
admin.site.register(People)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Neighboorhood)