# Generated by Django 4.1.3 on 2023-03-17 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_userinfo_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='index',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='序号'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='time',
            field=models.TimeField(auto_now=True, verbose_name='时间'),
        ),
    ]
