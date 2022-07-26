# Generated by Django 4.0.6 on 2022-07-25 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'address', 'verbose_name_plural': 'addresses'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'customer', 'verbose_name_plural': 'customers'},
        ),
        migrations.AlterModelOptions(
            name='drivinglicense',
            options={'verbose_name': 'driving license', 'verbose_name_plural': 'driving licenses'},
        ),
        migrations.AlterModelOptions(
            name='passport',
            options={'verbose_name': 'passport', 'verbose_name_plural': 'passports'},
        ),
        migrations.AlterField(
            model_name='address',
            name='cont',
            field=models.CharField(max_length=50, verbose_name='cont no'),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_four',
            field=models.CharField(max_length=200, verbose_name='address line four'),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_one',
            field=models.CharField(max_length=200, verbose_name='address line one'),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_three',
            field=models.CharField(max_length=200, verbose_name='address line three'),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_two',
            field=models.CharField(max_length=200, verbose_name='address line two'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=200, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='drivinglicense',
            name='country',
            field=models.CharField(max_length=200, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='drivinglicense',
            name='issued_date',
            field=models.DateField(verbose_name='issued date'),
        ),
        migrations.AlterField(
            model_name='drivinglicense',
            name='number',
            field=models.CharField(max_length=200, verbose_name='driving license number'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='country',
            field=models.CharField(max_length=200, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='expiry_date',
            field=models.DateField(verbose_name='expiry date'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='number',
            field=models.CharField(max_length=200, verbose_name='passport number'),
        ),
    ]
