# Generated by Django 3.2.8 on 2021-11-06 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_alter_users_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='avatar',
        ),
    ]
