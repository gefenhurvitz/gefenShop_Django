from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('products', views.getProducts, name="products"),
    path('products/<str:pk>/', views.getProduct, name="product"),
    
]
