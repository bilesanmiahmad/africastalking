# Generated by Django 2.1.7 on 2019-03-15 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ussd', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='userphone',
        ),
        migrations.AlterField(
            model_name='userdata',
            name='bags',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Number of bags'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='crop',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Crop'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='destination',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Destination'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='mobile_money',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Mobile money number'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='pickup',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Pickup Location'),
        ),
    ]
