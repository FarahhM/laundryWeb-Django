# Generated by Django 2.2.7 on 2020-01-22 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0003_auto_20200121_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='date_time',
        ),
        migrations.AddField(
            model_name='userorder',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
