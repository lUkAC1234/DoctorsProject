# Generated by Django 4.2.3 on 2023-08-07 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_videosmodel_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentsmodel',
            name='post',
        ),
        migrations.AddField(
            model_name='videosmodel',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='web.commentsmodel'),
        ),
        migrations.AlterField(
            model_name='videosmodel',
            name='slug',
            field=models.SlugField(),
        ),
    ]