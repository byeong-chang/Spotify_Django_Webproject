from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from music.models import Artist, Track, TrackBoard, ArtistBoard


# Create your views here.
@login_required(login_url='account:login')
def artist_vote(request, artist_board_id):
    artistboard = get_object_or_404(ArtistBoard, pk=artist_board_id)
    if request.user.id == artistboard.user_id:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        artistboard.like.add(request.user)
    return redirect("music:artist_page", artist_id=artistboard.artist_id)


@login_required(login_url='account:login')
def track_vote(request, track_board_id):
    trackboard = get_object_or_404(TrackBoard, pk=track_board_id)
    if request.user.id == trackboard.user_id:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다')
    else:
        trackboard.like.add(request.user)
    return redirect("music:track_page", track_id=trackboard.track_id)


@login_required(login_url='account:login')
def artist_follow(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)

    if artist in request.user.like_artist.all():
        artist.like.remove(request.user)
    else:
        artist.like.add(request.user)
    return redirect("music:artist_page", artist_id=artist_id)


@login_required(login_url='account:login')
def track_follow(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    if track in request.user.like_track.all():
        track.like.remove(request.user)
    else:
        track.like.add(request.user)
    return redirect("music:track_page", track_id=track_id)