# Generated by Django 2.2.7 on 2020-03-10 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0007_remove_orderitem_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='total',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
    ]