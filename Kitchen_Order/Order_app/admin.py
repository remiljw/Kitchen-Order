from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Orders

class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'user_type']
    list_filter = ['username','user_type']
    search_fields = ['username', 'user_type']
    fieldsets = [
        ('User', {'fields': ('username','password', 'user_type')})
    ]
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'order_details', 'order_date_time',
                    'taken_by', 'is_fulfilled', 'fulfilled_by']

 

admin.site.register(User, CustomUserAdmin)
admin.site.register(Orders, OrderAdmin)

# Register your models here.
