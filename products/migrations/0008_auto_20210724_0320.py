# Generated by Django 3.2.5 on 2021-07-24 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_home'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Paragraph',
            new_name='AboutUs',
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='people',
            new_name='name',
        ),
    ]
