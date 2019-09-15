from django.conf.urls import url
from django.conf.urls.static import static  
from django.conf import settings

from . import views


urlpatterns=[
    url('^$', views.nyumbani, name='nyumbani'),
    url(r'^about/$', views.about, name='about'),
    url(r'^search/', views.search_results, name='search_results'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)