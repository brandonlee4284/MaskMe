# Generated by Django 3.2.5 on 2021-07-27 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=10000)),
                ('other', models.CharField(max_length=10000)),
            ],
        ),
    ]
