# Generated by Django 2.0 on 2020-01-05 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_serviceinfo_status'),
        ('api', '0004_auto_20200104_1736'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Env',
            new_name='EnvInfo',
        ),
    ]
