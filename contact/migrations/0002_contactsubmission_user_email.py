# Generated by Django 3.2 on 2022-03-12 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactsubmission',
            name='user_email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
