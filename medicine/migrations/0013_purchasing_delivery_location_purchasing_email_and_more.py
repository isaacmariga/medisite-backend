# Generated by Django 4.0.2 on 2022-07-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0012_disease_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasing',
            name='delivery_location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchasing',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchasing',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]