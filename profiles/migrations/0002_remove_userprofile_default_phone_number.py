# Generated by Django 3.0.6 on 2020-05-18 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_phone_number',
        ),
    ]