from django.contrib import admin
from django.urls import path
from . import views, views1, views2, views3

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views1.home, name='home')
]