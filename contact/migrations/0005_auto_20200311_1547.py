# Generated by Django 3.0.3 on 2020-03-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20200311_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='document',
            field=models.FileField(upload_to='media'),
        ),
    ]
