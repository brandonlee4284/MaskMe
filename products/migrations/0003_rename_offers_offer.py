# Generated by Django 3.2.5 on 2021-07-24 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Offers',
            new_name='Offer',
        ),
    ]