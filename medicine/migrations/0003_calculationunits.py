# Generated by Django 4.0.2 on 2022-07-10 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_remove_user_name_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculationUnits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.CharField(blank=True, max_length=100, null=True)),
                ('sales', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('donations', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
