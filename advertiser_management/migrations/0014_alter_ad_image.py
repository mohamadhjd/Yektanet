# Generated by Django 4.0.2 on 2022-02-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0013_alter_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(null=True, upload_to='upload/'),
        ),
    ]