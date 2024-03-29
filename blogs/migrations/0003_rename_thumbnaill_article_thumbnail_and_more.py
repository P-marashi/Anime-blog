# Generated by Django 4.1.2 on 2022-11-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_article_creat_article_description_article_publish_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='thumbnaill',
            new_name='thumbnail',
        ),
        migrations.AlterField(
            model_name='article',
            name='creat',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'published')], max_length=1),
        ),
    ]
