# Generated by Django 2.2.7 on 2020-03-11 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0011_auto_20200311_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='service',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item_price',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]