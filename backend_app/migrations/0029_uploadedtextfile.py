# Generated by Django 4.1.5 on 2024-10-16 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0028_formtemplate_form_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedTextFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileowner', models.CharField(max_length=255)),
                ('filesender', models.CharField(max_length=255)),
                ('uploaded_text', models.TextField()),
                ('file_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
