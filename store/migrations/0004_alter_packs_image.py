# Generated by Django 3.2 on 2022-03-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20220321_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packs',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
