# Generated by Django 4.1.2 on 2023-01-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0019_remove_article_display_video_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ip', models.GenericIPAddressField(verbose_name='ip user')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='user_address',
            field=models.ManyToManyField(blank=True, related_name='user_address', to='blogs.ipaddress', verbose_name='user_ip'),
        ),
    ]