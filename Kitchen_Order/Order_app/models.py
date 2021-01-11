from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
USER_TYPES = (
    ('manager', 'Manager'),
    ('counter', 'Counter Staff'),
    ('kitchen', 'Kitchen Staff')
)

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    def __str__(self):
        return self.username

class Order(models.Model):
    order_number = models.IntegerField(default=0)
    order_details = models.CharField(max_length=200)
    order_date_time = models.DateTimeField()
    taken_by = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='Counter')
    fulfilled_by = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='Kitchen')