# Generated by Django 4.0.1 on 2022-01-18 10:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_article_commentnum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
        migrations.AddField(
            model_name='article',
            name='addDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期'),
        ),
        migrations.AddField(
            model_name='article',
            name='modifyDate',
            field=models.DateTimeField(auto_now=True, verbose_name='最后修改日期'),
        ),
    ]
