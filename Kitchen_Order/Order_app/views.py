from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
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
    if user.user_type == 'counter':
        message = 'You are not authorized to view this page'
        return render(request, 'kitchen.html', {'message': message})
    else:
        return render(request, 'kitchen.html')


def counter(request):
    user = request.user
    if user.user_type == 'kitchen':
        message = 'You are not authorized to view this page'
        return render(request, 'counters.html', {'message' : message})
    else:
         return render(request, 'counters.html')


def orders(request):
    return render(request, 'orders.html')


def manager(request):
    user = request.user
    if user.user_type != 'manager':
        message = 'You are not authorized to view this page'
        return render(request, 'manager.html', {'message' : message, 'user_form' : user_form})
    else:
        user_form = UserCreationForm
        # message = 'You are not authorized to view this page'
        return render(request, 'manager.html', {'user_form' : user_form})