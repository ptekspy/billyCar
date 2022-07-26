# Generated by Django 4.0.6 on 2022-07-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_customer_blocked'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='property_type',
            field=models.CharField(choices=[('CL', 'Client'), ('HO', 'Home'), ('BS', 'Business')], default='CL', max_length=2, verbose_name='property type'),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='', max_length=200, verbose_name='phone'),
            preserve_default=False,
        ),
    ]