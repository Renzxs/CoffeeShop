# Generated by Django 5.0.3 on 2024-04-12 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermodule', '0006_alter_order_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='voucher_code',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
