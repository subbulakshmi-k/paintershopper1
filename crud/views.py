from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

def h(request):
    return HttpResponse("Welcome to Kumaresan Painter Shop World!")

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def home(request):
    if request.user.is_authenticated:
        return redirect('welcome')
    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            error_message = "Invalid username or password."
            return render(request, 'home.html', {'error_message': error_message})
    return render(request, 'home.html')

def welcome(request):
    if not request.user.is_authenticated:
        return redirect('madikuthu_login')
    return render(request, 'welcome.html')

@login_required(login_url='/')
def services(request):
    return render(request, 'services.html')

from .models import Booking

def booknow(request):
    message = ''
    if request.method == 'POST' and 'booknow' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # Save booking info to database
        booking = Booking(username=username, email=email, password=password)
        booking.save()
        message = f"Booking successful for user: {username} with email: {email}"
    return render(request, 'booknow.html', {'message': message})

def about(request):
    return render(request, 'about.html')

def colors(request):
    return render(request, 'colors.html')

def madikuthu_login(request):
    error_message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'shobi' and password == 'shobi123':
            request.session['logged_in'] = True
            return redirect('home')
        else:
            error_message = 'Invalid username or password.'
    return render(request, 'login.html', {'error_message': error_message})
