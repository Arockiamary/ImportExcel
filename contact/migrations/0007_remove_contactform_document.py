# Generated by Django 3.0.3 on 2020-03-23 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20200312_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='document',
        ),
    ]
