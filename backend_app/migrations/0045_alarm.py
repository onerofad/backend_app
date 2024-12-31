# Generated by Django 5.1.3 on 2024-12-31 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0044_coursewebuser_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=255)),
                ('clockTime', models.CharField(default='', max_length=255)),
                ('aTime', models.CharField(default='', max_length=255)),
                ('yearformat', models.CharField(default='', max_length=255)),
                ('dcal', models.CharField(default='', max_length=255)),
                ('description', models.CharField(default='', max_length=255)),
            ],
        ),
    ]