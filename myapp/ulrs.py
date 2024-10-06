from django.contrib import admin
from django.urls import path
from . import views, views1, views2, views3
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views1.home, name='home'),
    path('register/', views3.register, name='register'),
    path('login/', views3.loginPage, name='login')
]