# Generated by Django 3.1.5 on 2021-01-12 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order_app', '0007_auto_20210112_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='fulfilled_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Kitchen', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orders',
            name='taken_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Counter', to=settings.AUTH_USER_MODEL),
        ),
    ]
