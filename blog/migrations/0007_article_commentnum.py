# Generated by Django 4.0.1 on 2022-01-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='commentNum',
            field=models.IntegerField(default=0, verbose_name='评论数'),
        ),
    ]
