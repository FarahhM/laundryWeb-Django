# Generated by Django 2.2.7 on 2020-01-21 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('laundry', '0002_auto_20200118_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='item',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='quantity',
        ),
        migrations.AddField(
            model_name='userorder',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='dry_clean',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dry+', to='laundry.Service'),
        ),
        migrations.AlterField(
            model_name='item',
            name='iron',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='iron+', to='laundry.Service'),
        ),
        migrations.AlterField(
            model_name='item',
            name='laundry',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='laundry+', to='laundry.Service'),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laundry.Item'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userorder',
            name='items',
            field=models.ManyToManyField(to='laundry.OrderItem'),
        ),
    ]
