from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm, NewOrder
from .models import User, Order
from datetime import datetime


# Create your views here.
@login_required
def dashboard(request):
    user = request.user
    if user.user_type == 'manager':
        response = redirect('manager')
    elif user.user_type == 'counter':
        response = redirect('counter')
    elif user.user_type == 'kitchen':
        response  = redirect('kitchen')
    else:
        template_name = 'registration/login.html'
        message = 'you do not have login access'

    return response


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
        form = NewOrder
        if request.method == 'POST':
            form = NewOrder(request.POST)
            if form.is_valid():
                new_order = form.save(commit=False)
                new_order.taken_by= user
                new_order.fulfilled_by = user
                new_order.order_date_time = datetime.now()
                new_order.save()
                return redirect
            else:
                form = NewOrder
        return render(request, 'counters.html', {'form': form})


def orders(request):
    all_orders = Order.objects.all()
    return render(request, 'orders.html', {'all_orders' : all_orders})


def manager(request):
    user = request.user
    if user.user_type != 'manager':
        message = 'You are not authorized to view this page'
        return render(request, 'manager.html', {'message' : message, 'user_form' : user_form})
    else:
        form = NewUserForm
        if request.method == 'POST':
            form = NewUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect
            else:
                form = NewUserForm
        return render(request, 'manager.html', {'form' : form})
