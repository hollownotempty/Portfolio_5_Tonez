# Generated by Django 3.2 on 2022-02-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_packs_demo_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packs',
            name='demo_link',
            field=models.TextField(max_length=1000),
        ),
    ]