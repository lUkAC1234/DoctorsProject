# Generated by Django 4.2.3 on 2023-08-07 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videosmodel',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
