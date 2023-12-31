# Generated by Django 5.0 on 2023-12-12 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('suite', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('confirmpassword', models.CharField(max_length=255)),
                ('socialsecurity', models.CharField(max_length=255)),
                ('confirmsocialsecurity', models.CharField(max_length=255)),
                ('dob', models.DateField(auto_now_add=True)),
                ('profileimage', models.TextField()),
                ('cardimagefront', models.TextField()),
                ('carfimageback', models.TextField()),
            ],
        ),
    ]
