# Generated by Django 4.0.2 on 2022-02-18 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0004_alter_ad_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='image',
        ),
    ]
