# Generated by Django 4.0.2 on 2022-02-22 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0024_remove_ad_clicks_remove_ad_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='view',
            name='time',
            field=models.DateTimeField(),
        ),
    ]