from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User

# Create your views here.
@login_required
def dashboard(request):
    user = request.user
    if user.user_type == 'manager':
        template_name = 'manager.html'
    elif user.user_type == 'counter':
        template_name = 'counters.html'
    elif user.user_type == 'kitchen':
        template_name = 'kitchen.html'
    else:
        template_name = 'registration/login.html'
        message = 'you do not have login access'
    return render(request, template_name)


def kitchen(request):
    user = request.user
    if user.user_type != 'manager' or 'kitchen':
        message = 'You are not authorized to view this page'
    return render(request, 'kitchen.html', {'message': message})


def counter(request):
    user = request.user
    if user.user_type != 'manager' or 'counter':
        message = 'You are not authorized to view this page'
    return render(request, 'counters.html', {'message' : message})


def orders(request):
    return render(request, 'orders.html')


def manager(request):
    user = request.user
    if user.user_type != 'manager':
        message = 'You are not authorized to view this page'
    return render(request, 'manager.html', {'message' : message})