from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView )



urlpatterns = [
    path('',views.home, name='home'),
    path('blogging', PostListView.as_view(), name='blogging'),
    path('businesses', views.businesses, name='businesses'),
    path('search/', views.search_results, name='search_results'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about'),
]
