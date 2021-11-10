from django.contrib import admin
from django.urls import path, include
from inventory import views


urlpatterns = [
    path('main', views.inventory, name='inventory'),
    #path('entry', views.entry, name='entry'),
    path('', views.home, name='home'),
    path('entry', views.entry, name="entry"),
    path('receipt/<str:pk>/', views.products, name="receipt")

    #/<str:pk>/
    
    
]

