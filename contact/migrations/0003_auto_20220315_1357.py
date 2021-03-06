# Generated by Django 3.2 on 2022-03-15 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0002_contactsubmission_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactsubmission',
            old_name='user_email',
            new_name='email',
        ),
        migrations.AddField(
            model_name='contactsubmission',
            name='full_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactsubmission',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
