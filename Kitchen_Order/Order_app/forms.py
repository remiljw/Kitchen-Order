from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Order, USER_TYPES

class NewUserForm(UserCreationForm):
    password2 = None

    class Meta:
        model = User
        fields = ('username','password1', 'user_type')

class NewOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_number', 'order_details')