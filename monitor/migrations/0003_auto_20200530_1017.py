# Generated by Django 3.0.2 on 2020-05-30 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20200530_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='real_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='time_zone',
            new_name='tz',
        ),
    ]
