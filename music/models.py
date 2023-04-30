from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Artist(models.Model):
    artist_id = models.CharField(max_length=200, primary_key=True)
    artist_name = models.CharField(max_length=200)
    artist_popularity = models.CharField(max_length=200)
    artist_followers = models.IntegerField()
    artist_image_link = models.CharField(max_length=200, default=None)
    like = models.ManyToManyField(User, related_name='like_artist')


class Track(models.Model):
    track_name = models.CharField(max_length=200)
    track_id = models.CharField(max_length=200, primary_key=True)
    track_popularity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    artist_name = models.CharField(max_length=200, default=None)
    track_image_link = models.CharField(max_length=200, default=None)
    track_release_date = models.DateField(null=True, default=None)
    # 유사곡
    similar_track_id1 = models.CharField(max_length=200, default=None)
    similar_track_id2 = models.CharField(max_length=200, default=None)
    similar_track_id3 = models.CharField(max_length=200, default=None)
    similar_track_id4 = models.CharField(max_length=200, default=None)
    similar_track_id5 = models.CharField(max_length=200, default=None)
    like = models.ManyToManyField(User, related_name='like_track')


class ArtistBoard(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='like_artistBoard')
    content = models.TextField()
    create_date = models.DateTimeField()  # 날짜와 시간


class TrackBoard(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='like_TrackBoard')
    content = models.TextField()
    create_date = models.DateTimeField()  # 날짜와 시간
