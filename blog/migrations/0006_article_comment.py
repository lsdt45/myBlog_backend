# Generated by Django 4.0.1 on 2022-01-18 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_likenum_alter_article_introduction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.TextField(default='', verbose_name='评论'),
        ),
    ]
