# Generated by Django 3.2 on 2022-03-22 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField(max_length=9000)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
