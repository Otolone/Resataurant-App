# Generated by Django 2.1.7 on 2019-03-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_restaurantloction_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantloction',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='restaurantloction',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
