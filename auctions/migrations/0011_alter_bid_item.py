# Generated by Django 3.2.4 on 2022-03-24 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20220324_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='auctions.item'),
        ),
    ]
