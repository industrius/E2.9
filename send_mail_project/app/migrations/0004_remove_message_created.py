# Generated by Django 3.1.2 on 2020-10-03 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201003_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='created',
        ),
    ]
