# Generated by Django 4.1.3 on 2023-09-13 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
