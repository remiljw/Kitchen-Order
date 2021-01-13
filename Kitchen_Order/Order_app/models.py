from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
USER_TYPES = (
    ('manager', 'Manager'),
    ('counter_staff', 'Counter Staff'),
    ('kitchen_staff', 'Kitchen Staff')
)

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    def __str__(self):
        return self.username



class Order(models.Model):
    order_number = models.IntegerField(default='', unique=True)
    order_details = models.TextField(max_length=200)
    order_date_time = models.DateTimeField(auto_now_add=True)
    taken_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Counter')
    is_fulfilled = models.BooleanField(default=False)
    fulfilled_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='Kitchen')

    def __str__(self):
        return str(self.order_number)