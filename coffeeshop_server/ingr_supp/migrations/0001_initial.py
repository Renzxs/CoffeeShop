# Generated by Django 5.0.4 on 2024-04-10 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingr_name', models.CharField(max_length=50)),
                ('ingr_quant', models.IntegerField(default=0)),
                ('ingr_desc', models.CharField(max_length=50)),
                ('ingr_catg', models.CharField(max_length=50)),
                ('ingr_cost', models.FloatField(default=0.0)),
                ('ingr_suppNo', models.CharField(max_length=50)),
                ('ingr_exp', models.CharField(max_length=50)),
                ('ingr_batch', models.CharField(default='00001', max_length=5)),
                ('ingr_date', models.DateField()),
                ('ingr_act', models.BooleanField(default=True)),
            ],
        ),
    ]