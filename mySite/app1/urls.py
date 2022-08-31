
from django.contrib import admin
from django.urls import path

app_name = 'appa1'

urlpatterns = [
    path('', views.index),
]