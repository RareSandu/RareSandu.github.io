# Generated by Django 3.2.4 on 2022-03-24 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20220323_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='Name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bid',
            name='Number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
