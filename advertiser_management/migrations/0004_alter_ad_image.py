# Generated by Django 4.0.2 on 2022-02-18 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0003_alter_ad_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]