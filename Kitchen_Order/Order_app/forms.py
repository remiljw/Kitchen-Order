from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Order

class NewUserForm(UserCreationForm):
    password2 = None

    class Meta:
        model = User
        fields = ('username','password1', 'user_type')

class NewOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_number', 'order_details')

class UpdateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_number', 'order_details', 'is_fulfilled')