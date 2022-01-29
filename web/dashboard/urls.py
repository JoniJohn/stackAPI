from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('articles', views.dashboard2, name='dashboard2'),
]