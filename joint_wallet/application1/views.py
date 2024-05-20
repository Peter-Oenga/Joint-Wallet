from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def inner_page(request):
    return render(request, "inner-page.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have succesfully logged in!')
            return redirect('index')
        
        else:
            messages.success(request, "There was a problem please try again later")
            return redirect('login')

    else:
        return render(request, "login.html", {})
    

def logout_user(request):
    pass

def register(request):
    return render(request, "register.html", {})