# Generated by Django 2.0 on 2019-12-14 20:58

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0002_departmentinfo_projectinfo_versioninfo'),
        ('requirement', '0002_requirementinfo_requirementtask_tasktimes'),
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Bug标题')),
                ('detail', DjangoUeditor.models.UEditorField(default='', verbose_name='Bug详情')),
                ('reporter', models.CharField(default='', max_length=10, verbose_name='提单人')),
                ('solver', models.CharField(default='', max_length=10, verbose_name='指派给')),
                ('level', models.CharField(choices=[('zm', '致命'), ('yz', '严重'), ('yb', '一般'), ('ts', '提示')], default='yb', max_length=10, verbose_name='优先级')),
                ('env', models.CharField(choices=[('test', '测试环境'), ('gray', '灰度环境'), ('online', '线上环境')], default='test', max_length=50, verbose_name='环境')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.DateField(default=datetime.datetime.now, verbose_name='修改时间')),
                ('status', models.CharField(choices=[('Open', '打开'), ('ReOpen', '重新打开'), ('Fixed', '已解决'), ('Rejected', '无需解决'), ('Closed', '已关闭')], default='Open', max_length=5, verbose_name='用例状态')),
                ('belong_requirement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='requirement.RequirementInfo', verbose_name='所属需求')),
                ('belong_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.VersionInfo', verbose_name='所属版本')),
            ],
            options={
                'verbose_name': 'bug信息',
                'verbose_name_plural': 'bug信息',
            },
        ),
        migrations.CreateModel(
            name='BugRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(default='', max_length=10, verbose_name='操作者')),
                ('desc', models.CharField(default='', max_length=50, verbose_name='操作说明')),
                ('status_change', models.CharField(default='', max_length=50, verbose_name='状态变更')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.DateField(default=datetime.datetime.now, verbose_name='修改时间')),
                ('belong_bug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bugs.BugInfo', verbose_name='所属Bug')),
            ],
            options={
                'verbose_name': ' Bug操作记录',
                'verbose_name_plural': ' Bug操作记录',
            },
        ),
    ]
