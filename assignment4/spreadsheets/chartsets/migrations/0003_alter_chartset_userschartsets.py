# Generated by Django 3.2.9 on 2021-12-05 00:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chartsets', '0002_chartset_userschartsets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartset',
            name='userschartsets',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Имеют доступ'),
        ),
    ]
