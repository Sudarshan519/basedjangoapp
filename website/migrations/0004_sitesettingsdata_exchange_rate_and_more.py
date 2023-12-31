# Generated by Django 4.1.3 on 2023-08-26 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_sitesettingsdata_steps_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettingsdata',
            name='exchange_rate',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='sitesettingsdata',
            name='service_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='stepstostartup',
            name='sitesetting',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='website.sitesettingsdata'),
        ),
        migrations.AlterField(
            model_name='whychooseus',
            name='sitesetting',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='whyus', to='website.sitesettingsdata'),
        ),
    ]
