"""Kitchen_Order URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Order_app.views import dashboard, manager, orders, kitchen, counter, fulfill_order
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', dashboard, name='home'),
    path('manager', manager, name='manager_page'),
    path('orders', orders, name='order_page'),
    path('kitchen', kitchen, name='kitchen_page'),
    path('counter', counter, name='counter_page'),
    path('fulfill/order/<int:id>/', fulfill_order, name='fulfill_order')
]
