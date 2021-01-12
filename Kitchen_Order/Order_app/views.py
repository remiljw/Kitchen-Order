from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm, NewOrderForm, UpdateOrderForm
from .models import User, Orders
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
    return response


def kitchen(request):
    user = request.user
    if user.user_type == 'counter':
        message = 'You are not authorized to view this page'
        return render(request, 'kitchen.html', {'message': message})
    else:
        orders = Orders.objects.filter(is_fulfilled=False)
        return render(request, 'kitchen.html', {'orders':orders})


def counter(request):
    user = request.user
    if user.user_type == 'kitchen':
        message = 'You are not authorized to view this page'
        return render(request, 'counters.html', {'message' : message})
    else:
        form = NewOrderForm
        if request.method == 'POST':
            form = NewOrderForm(request.POST)
            if form.is_valid():
                new_order = form.save(commit=False)
                new_order.taken_by= user
                new_order.order_date_time = datetime.now()
                new_order.save()
                return redirect('counter')
            else:
                form = NewOrderForm
        return render(request, 'counters.html', {'form': form})


def orders(request):
    all_orders = Orders.objects.all()
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
                return redirect('/')
            else:
                form = NewUserForm
        return render(request, 'manager.html', {'form' : form})


def fulfill_order(request, id):
    user = request.user
    obj = Orders.objects.get(id=id)
    form = UpdateOrderForm(request.POST or None, instance=obj)
    if form.is_valid():
        update_order = form.save(commit=False)
        update_order.fulfilled_by = user
        update_order.save()
        return redirect('kitchen')
    else:
        form = UpdateOrderForm(instance=obj)
    return render(request, 'fulfill.html', {'form': form})