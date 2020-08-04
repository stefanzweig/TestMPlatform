# Generated by Django 2.0 on 2020-01-07 16:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_localparameterinfo_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalparameterinfo',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='globalparameterinfo',
            name='related_case',
            field=models.CharField(default='', max_length=10, verbose_name='关联项目ID'),
        ),
        migrations.AddField(
            model_name='globalparameterinfo',
            name='type',
            field=models.CharField(choices=[('1', 'key-value'), ('2', 'SQL'), ('3', '测试用例')], default='1', max_length=10, verbose_name='参数类型'),
        ),
        migrations.AddField(
            model_name='globalparameterinfo',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间'),
        ),
        migrations.AddField(
            model_name='localparameterinfo',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='localparameterinfo',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='globalparameterinfo',
            name='belong_env',
            field=models.CharField(default='', max_length=50, verbose_name='关联环境ID'),
        ),
        migrations.AlterField(
            model_name='localparameterinfo',
            name='belong_env_id',
            field=models.CharField(default='', max_length=10, verbose_name='关联环境ID'),
        ),
        migrations.AlterField(
            model_name='localparameterinfo',
            name='belong_project_id',
            field=models.CharField(default='', max_length=10, verbose_name='关联项目ID'),
        ),
    ]
