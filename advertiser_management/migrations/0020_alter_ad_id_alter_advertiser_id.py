# Generated by Django 4.0.2 on 2022-02-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertiser_management', '0019_alter_ad_id_alter_advertiser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='advertiser',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]