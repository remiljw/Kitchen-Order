# Generated by Django 3.1.5 on 2021-01-12 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order_app', '0006_auto_20210112_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(default='')),
                ('order_details', models.TextField(max_length=200)),
                ('order_date_time', models.DateTimeField(auto_now_add=True)),
                ('is_fulfilled', models.BooleanField(default=False)),
                ('fulfilled_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Kitchen', to=settings.AUTH_USER_MODEL)),
                ('taken_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Counter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
