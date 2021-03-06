# Generated by Django 3.1.5 on 2021-01-12 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order_app', '0005_auto_20210112_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(default='', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='taken_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Counter', to=settings.AUTH_USER_MODEL),
        ),
    ]
