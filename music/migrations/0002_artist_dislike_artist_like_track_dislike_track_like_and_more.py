# Generated by Django 4.2 on 2023-04-26 23:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='dislike',
            field=models.ManyToManyField(related_name='dislike_artist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artist',
            name='like',
            field=models.ManyToManyField(related_name='like_artist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='track',
            name='dislike',
            field=models.ManyToManyField(related_name='dislike_track', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='track',
            name='like',
            field=models.ManyToManyField(related_name='like_track', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='artistboard',
            name='dislike',
            field=models.ManyToManyField(related_name='dislike_artistBoard', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='artistboard',
            name='like',
            field=models.ManyToManyField(related_name='like_artistBoard', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trackboard',
            name='dislike',
            field=models.ManyToManyField(related_name='dislike_TrackBoard', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trackboard',
            name='like',
            field=models.ManyToManyField(related_name='like_TrackBoard', to=settings.AUTH_USER_MODEL),
        ),
    ]