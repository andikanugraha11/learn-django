# Generated by Django 2.1.4 on 2018-12-28 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudex', '0002_auto_20181226_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='name',
        ),
    ]
