# Generated by Django 3.2 on 2022-02-26 12:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220225_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='packs',
            name='demo_link',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
