# Generated by Django 4.1.3 on 2023-02-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_article_accessnum_article_readnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='coverPath',
            field=models.CharField(default='', max_length=100, verbose_name='封面地址'),
            preserve_default=False,
        ),
    ]
