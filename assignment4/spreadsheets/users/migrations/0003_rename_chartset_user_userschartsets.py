# Generated by Django 3.2.9 on 2021-11-28 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_users_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='chartset',
            new_name='userschartsets',
        ),
    ]