from django.shortcuts import render
from django.contrib import admin
from . import views
from django.urls import path
from django.contrib import admin

admin.site.site_header = "REC Symposium"
admin.site.site_title = "Admin Panel Team O(1)"
admin.site.index_title = "REC Tesseract"

urlpatterns = [
    path('', views.index),
    path('home/',views.home),
    path('login/', views.user_login),
    path('signup/', views.user_signup),
]
