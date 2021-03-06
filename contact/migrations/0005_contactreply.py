# Generated by Django 3.2 on 2022-03-20 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_remove_contactsubmission_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=300)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.contactsubmission')),
            ],
        ),
    ]
