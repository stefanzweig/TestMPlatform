# Generated by Django 2.0 on 2020-01-10 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20200110_1504'),
    ]

    operations = [
        migrations.RenameField(
            model_name='globalparameterinfo',
            old_name='related_case_id',
            new_name='related_case',
        ),
    ]