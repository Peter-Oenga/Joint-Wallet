from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def inner_page(request):
    return render(request, "inner-page.html", {})

def portfolio(request):
    return render(request, "portfolio-details.html", {})

def login_user(request):
    return render(request, "login.html", {})

def logout_user(request):
    pass
