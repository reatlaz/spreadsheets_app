# Generated by Django 3.2.9 on 2021-11-29 17:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chartsets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='chartset',
            name='userschartsets',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
    ]
