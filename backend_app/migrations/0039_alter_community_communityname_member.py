# Generated by Django 5.1.3 on 2024-11-20 22:01

import backend_app.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0038_community_delete_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='communityname',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memberEmail', models.CharField(max_length=255)),
                ('memberRole', models.CharField(max_length=255)),
                ('accessnumber', models.CharField(default=backend_app.models.getRandom, max_length=255)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_app.community', to_field='communityname')),
            ],
        ),
    ]