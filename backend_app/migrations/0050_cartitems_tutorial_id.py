# Generated by Django 5.1.3 on 2025-02-21 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0049_cartitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='tutorial_id',
            field=models.IntegerField(default=0),
        ),
    ]
