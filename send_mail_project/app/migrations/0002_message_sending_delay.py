# Generated by Django 3.1.2 on 2020-10-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sending_delay',
            field=models.PositiveIntegerField(default=0, verbose_name='Задержка отправки письма'),
        ),
    ]
