# Generated by Django 4.2 on 2023-05-21 04:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_rename_artist_id_track_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='expires_in',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
