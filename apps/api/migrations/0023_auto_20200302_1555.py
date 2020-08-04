# Generated by Django 2.2.4 on 2020-03-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20200110_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apicaseinfo',
            name='type',
            field=models.CharField(choices=[('0', '公共用例'), ('1', 'CI'), ('2', '非CI'), ('3', '删除')], default='1', max_length=10, verbose_name='用例类型'),
        ),
        migrations.AlterField(
            model_name='operationinfo',
            name='type',
            field=models.CharField(choices=[('0', '用例'), ('1', 'SQL'), ('2', '等待')], default='0', max_length=10, verbose_name='操作类型'),
        ),
    ]
