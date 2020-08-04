# Generated by Django 2.0 on 2019-12-29 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requirement', '0003_auto_20191228_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirementinfo',
            name='status',
            field=models.CharField(choices=[('0', '删除'), ('1', '新建'), ('2', '开发中'), ('3', '测试验收'), ('4', '验收完成'), ('5', '暂停')], default='1', max_length=10, verbose_name='需求状态'),
        ),
    ]
