# Generated by Django 4.1.5 on 2024-10-13 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0025_remove_student_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=127)),
                ('last_name', models.CharField(max_length=127)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
