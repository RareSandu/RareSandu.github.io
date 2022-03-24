# Generated by Django 3.2.4 on 2021-09-10 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_bid_bidder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('product', models.ManyToManyField(related_name='watchlist', to='auctions.Item')),
            ],
        ),
    ]
