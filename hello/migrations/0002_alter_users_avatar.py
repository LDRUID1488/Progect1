# Generated by Django 3.2.8 on 2021-11-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.ImageField(null=True, upload_to='logo_user', verbose_name='Фото'),
        ),
    ]