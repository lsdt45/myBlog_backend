# Generated by Django 4.1.3 on 2023-03-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_userinfo_ad_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='time',
            field=models.TimeField(auto_now=True, verbose_name='时间'),
        ),
    ]
