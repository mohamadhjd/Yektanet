# Generated by Django 4.0.2 on 2022-02-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0010_alter_ad_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
