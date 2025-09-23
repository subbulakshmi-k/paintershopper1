from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('services/', views.services, name='services'),
    path('colors/', views.colors, name='colors'),
    path('about/', views.about, name='about'),
    path('booknow/', views.booknow, name='booknow'),
]
