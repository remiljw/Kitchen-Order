from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import User, Order

class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'user_type']
    list_filter = ['username','user_type']
    search_fields = ['username', 'user_type']
    fieldsets = [
        ('User', {'fields': ('username','user_type')})
    ]

 

admin.site.register(User, CustomUserAdmin)
admin.site.register(Order)

# Register your models here.
