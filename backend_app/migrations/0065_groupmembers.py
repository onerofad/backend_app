# Generated by Django 5.2.4 on 2025-07-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0064_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupId', models.CharField(max_length=255)),
                ('membername', models.CharField(max_length=255)),
            ],
        ),
    ]
