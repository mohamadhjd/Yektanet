# Generated by Django 4.0.2 on 2022-02-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0021_view_click'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='time',
            field=models.DateTimeField(),
        ),
    ]