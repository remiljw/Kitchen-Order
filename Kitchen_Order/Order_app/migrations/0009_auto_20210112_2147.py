# Generated by Django 3.1.5 on 2021-01-12 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order_app', '0008_auto_20210112_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_number',
            field=models.IntegerField(default='', unique=True),
        ),
    ]
