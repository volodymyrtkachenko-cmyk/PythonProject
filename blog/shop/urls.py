from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop_index'),
    path('category/<slug:slug>/', views.category_view, name='category_view'),
    path('product/<slug:slug>/', views.product_view, name='product_view'),
]