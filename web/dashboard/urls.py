from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('questions', views.dashboard, name='dashboard'),
    path('articles', views.dashboard2, name='dashboard2'),
    path('', views.dashboard3, name='dashboard3'),
]