# Generated by Django 4.1.2 on 2022-12-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_article_ve_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(verbose_name='متن زیر عکس'),
        ),
    ]