# Generated by Django 4.2 on 2023-05-21 04:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_user_expires_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expires_in',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]