
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    expires_in = models.DateTimeField(default=timezone.now)

class GlobalTop50(models.Model):
    track_id = models.CharField(max_length=255, primary_key=True)
    disc_number = models.IntegerField()
    created_date = models.DateTimeField(default="")

class Artist(models.Model):
    artist_id = models.CharField(max_length=255, primary_key=True)
    artist_name = models.CharField(max_length=255)
    artist_popularity = models.IntegerField()
    artist_followers = models.IntegerField()
    artist_image_link = models.TextField()
    created_date = models.DateTimeField(default="")
    like = models.ManyToManyField(User, related_name='like_artist')


class Track(models.Model):
    track_id = models.CharField(max_length=255, primary_key=True)
    track_name = models.CharField(max_length=255)
    track_popularity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    track_image_link = models.CharField(max_length=255, default=None)
    track_release_date = models.DateField(null=True, default=None)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default="")
    like = models.ManyToManyField(User, related_name='like_track')
    track_uri = models.CharField(max_length=255,default=None)
    # 유사곡
    # similar_track_id1 = models.CharField(max_length=200, default=None)
    # similar_track_id2 = models.CharField(max_length=200, default=None)
    # similar_track_id3 = models.CharField(max_length=200, default=None)
    # similar_track_id4 = models.CharField(max_length=200, default=None)
    # similar_track_id5 = models.CharField(max_length=200, default=None)


class ArtistBoard(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='like_artistBoard')
    content = models.TextField()
    create_date = models.DateTimeField(default="")  # 날짜와 시간


class TrackBoard(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='like_TrackBoard')
    content = models.TextField()
    create_date = models.DateTimeField(default="")  # 날짜와 시간

class MusicAudio(models.Model):
    track_id = models.CharField(max_length=255, primary_key=True)
    danceability = models.FloatField()
    energy = models.FloatField()
    loudness = models.FloatField()
    mode = models.SmallIntegerField()
    speechiness = models.FloatField()
    acousticness = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    valence = models.FloatField()
    tempo = models.FloatField()
    created_date = models.DateTimeField(default="")