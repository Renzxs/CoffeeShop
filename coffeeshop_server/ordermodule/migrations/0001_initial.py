# Generated by Django 5.0.4 on 2024-04-10 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rider_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_amount', models.FloatField(null=True)),
                ('customer_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ordermodule.customer')),
                ('product_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ordermodule.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('total_amount', models.FloatField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('location_address', models.CharField(default='', max_length=250)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('method', models.CharField(default='Delivery', max_length=50)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('customer_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ordermodule.customer')),
                ('product_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ordermodule.product')),
                ('rider_id', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='ordermodule.rider')),
            ],
        ),
    ]
