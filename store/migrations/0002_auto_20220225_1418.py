# Generated by Django 3.2 on 2022-02-25 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='category_name',
            new_name='friendly_name',
        ),
        migrations.AddField(
            model_name='categories',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
    ]
