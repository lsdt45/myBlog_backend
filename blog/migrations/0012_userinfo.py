# Generated by Django 4.1.3 on 2023-03-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_article_coverpath'),
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50, verbose_name='IP地址')),
                ('ad_info', models.CharField(max_length=50, verbose_name='地区信息')),
            ],
        ),
    ]
