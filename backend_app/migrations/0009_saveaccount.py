# Generated by Django 5.0 on 2024-02-13 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0008_remove_localtransfer_accountbal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('accountnumber', models.CharField(max_length=255)),
            ],
        ),
    ]
