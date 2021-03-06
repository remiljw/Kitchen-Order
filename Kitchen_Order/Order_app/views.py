from django.shortcuts import render, redirect,  HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm, NewOrderForm, UpdateOrderForm
from .models import User, Order
from datetime import datetime
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.
@login_required
def dashboard(request):
    #Redirects users to their respective dashboards
    user = request.user
    if user.user_type == 'counter_staff':
        response = redirect('counter_page')
        return response
    elif user.user_type == 'kitchen_staff':
        response  = redirect('kitchen_page')
        return response
    elif user.user_type == 'manager': 
        response = redirect('manager_page')
        return response
    else:
        messages.error(request,  'You are not authorized to login, contact your manager')
        return redirect('login')


#Kitchen Staff Page
@login_required
def kitchen(request):
    user = request.user
    if user.user_type != 'kitchen_staff' and user.user_type != 'manager':
        message = 'You are not authorized to view this page'
        return render(request, 'kitchen.html', {'message': message})
    else:
        orders = Order.objects.filter(is_fulfilled=False)
        return render(request, 'kitchen.html', {'orders':orders})

#Counter Staff Page
@login_required
def counter(request):
    message = {}
    user = request.user
    if user.user_type != 'counter_staff' and user.user_type != 'manager':
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
                message['success'] = 'Order Taken Successfully'
                return JsonResponse(message)
            message['error'] = form.errors
            message['err_code'] = 400
            return JsonResponse(message)
        return render(request, 'counters.html', {'form': form})

#Orders Page
def orders(request):
    all_orders = Order.objects.all()
    return render(request, 'orders.html', {'all_orders' : all_orders})

#Manager's Page
@login_required
def manager(request):
    user = request.user
    if user.user_type != 'manager':
        message = 'You are not authorized to view this page'
        return render(request, 'manager.html', {'message' : message})
    else:
        form = NewUserForm
        if request.method == 'POST':
            form = NewUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User Created Successfully')
                return redirect('/')
        return render(request, 'manager.html', {'form' : form})

#Kitchen Staff Page
@login_required
def fulfill_order(request, id):
    user = request.user
    obj = Order.objects.get(order_number=id)
    form = UpdateOrderForm(request.POST or None, instance=obj)
    if form.is_valid():
        update_order = form.save(commit=False)
        update_order.fulfilled_by = user
        update_order.save()
        messages.success(request, 'Order Fulfilled Succesfully')
        return redirect('kitchen_page')
    else:
        form = UpdateOrderForm(instance=obj)
    return render(request, 'fulfill.html', {'form': form})