# Generated by Django 2.2.4 on 2020-05-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_remove_apicaseinfo_run_after_operation'),
    ]

    operations = [
        migrations.AddField(
            model_name='apicaseinfo',
            name='run_after_operation',
            field=models.CharField(default='', max_length=100, verbose_name='执行后操作'),
        ),
    ]
