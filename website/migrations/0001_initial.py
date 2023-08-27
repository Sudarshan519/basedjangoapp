# Generated by Django 4.1.3 on 2023-08-26 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StepsToStartUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TermsAndConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='WhatYouCanDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='WhyChooseUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSettingsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.stepstostartup')),
                ('terms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.termsandconditions')),
                ('what_you_can_do', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.whatyoucando')),
                ('whyus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='why_us', to='website.whychooseus')),
            ],
        ),
    ]
