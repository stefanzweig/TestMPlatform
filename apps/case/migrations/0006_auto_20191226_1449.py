# Generated by Django 2.0 on 2019-12-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0005_auto_20191225_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcasesuit',
            name='requirement_id',
            field=models.CharField(default='', max_length=5, verbose_name='关联需求ID'),
        ),
    ]