# Generated by Django 5.0.3 on 2024-04-11 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermodule', '0003_remove_order_product_id_remove_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.FloatField(null=True),
        ),
    ]