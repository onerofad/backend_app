# Generated by Django 5.2.4 on 2025-07-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0063_alter_tabledata_value21_alter_tabledata_value22_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=255)),
                ('owner', models.CharField(max_length=255)),
            ],
        ),
    ]
