# Generated by Django 4.1.3 on 2023-09-11 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_app', '0002_alter_movie_movie_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='TVSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Banner Image')),
                ('url', models.CharField(max_length=256)),
                ('youtube_trailer_id', models.CharField(max_length=256)),
                ('desc', models.CharField(blank=True, max_length=256, null=True)),
                ('price', models.CharField(blank=True, max_length=256, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('trending', models.CharField(choices=[('Trending', 'Trending'), ('Latest', 'Latest')], default='Trending', max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Episodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=256, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Banner Image')),
                ('youtube_trailer_id', models.CharField(max_length=256)),
                ('desc', models.CharField(blank=True, max_length=256, null=True)),
                ('movie_path', models.FileField(blank=True, null=True, upload_to='series/')),
                ('tv_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streaming_app.tvseries')),
            ],
        ),
    ]