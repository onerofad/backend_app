# Generated by Django 5.0 on 2024-02-04 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0007_localtransfer_to_fname_localtransfer_to_lname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localtransfer',
            name='accountbal',
        ),
        migrations.RemoveField(
            model_name='localtransfer',
            name='accounttype',
        ),
    ]
