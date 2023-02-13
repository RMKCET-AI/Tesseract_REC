from django.shortcuts import render
from django.contrib import admin
from . import views
from django.urls import path
from django.contrib import admin

admin.site.site_header = "REC Symposium"
admin.site.site_title = "Tesseract Admin Panel"
admin.site.index_title = "Dashboard Tesseract"

urlpatterns = [
    path('', views.index),
    path('login/', views.user_login),
    path('signup/', views.user_signup),
]
