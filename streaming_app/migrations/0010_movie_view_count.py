# Generated by Django 4.2.1 on 2023-10-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_app', '0009_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]