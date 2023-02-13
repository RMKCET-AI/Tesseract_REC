from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, 'cube/base.html')


def user_login(request):
    return render(request, 'cube/login.html')

def user_signup(request):
    return render(request, 'cube/signup.html')