from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages, auth
from .models import User, Data


# Create your views here.

def home(request):
    return render(request, 'home.html')


def form(request):
    return render(request, 'form.html')


def mpage(request):
    return render(request, 'mpage.html')


def ulogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.info(request, "User created")
                return redirect('ulogin')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def form(request):
    if request.method == 'POST':
        message = 'Application accepted. Click <a href="/">Home</a> to return to the home page.'
        return render(request, 'form.html', {'message': message})
    return render(request, 'form.html')


def ulogout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('/')
