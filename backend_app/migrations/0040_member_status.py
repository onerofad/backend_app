# Generated by Django 5.1.3 on 2024-11-21 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0039_alter_community_communityname_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='status',
            field=models.CharField(default='pending', max_length=255),
        ),
    ]
