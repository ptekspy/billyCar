# Generated by Django 4.0.6 on 2022-07-25 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200)),
                ('license', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=200)),
            ],
        ),
    ]
