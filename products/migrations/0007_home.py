# Generated by Django 3.2.5 on 2021-07-24 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_clearance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=10000)),
                ('video_url', models.CharField(max_length=10000)),
            ],
        ),
    ]