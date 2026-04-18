from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/<slug:slug>', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:slug>', views.category, name='category'),
    path('tag/<slug:slug>', views.tag, name='tag'),
]