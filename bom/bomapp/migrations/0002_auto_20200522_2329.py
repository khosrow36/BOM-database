# Generated by Django 3.0.6 on 2020-05-22 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bomapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Parts',
            new_name='Part',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='Suppliers',
            new_name='Supplier',
        ),
    ]
