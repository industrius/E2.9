# Generated by Django 3.1.2 on 2020-10-04 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201004_0556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='success',
        ),
        migrations.AddField(
            model_name='message',
            name='status',
            field=models.CharField(default='Не отправлено', max_length=10, verbose_name='Статус'),
        ),
    ]
