# Generated by Django 3.0.6 on 2020-05-18 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20200518_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='quantity',
        ),
    ]
