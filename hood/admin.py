from django.contrib import admin
from django.conf.urls import url,include
from django.contrib.auth import views

# Register your models here.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('hood.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
]