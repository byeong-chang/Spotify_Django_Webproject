from django.shortcuts import render, redirect
from .models import Artist, Track, ArtistBoard, TrackBoard,User
from .forms import TrackAnswerForm, ArtistAnswerForm
from django.utils import timezone
from django.core.paginator import Paginator


# 검색창 검색
def search(request):
    query = request.GET.get('q')
    artist_boards = ArtistBoard.objects.order_by('-create_date')[:7]
    track_boards = TrackBoard.objects.order_by('-create_date')[:7]
    return render(request, 'music/search.html', {'query': query, 'artist_boards' : artist_boards, 'track_boards' : track_boards})


# 검색창 결과 - 가수, 음악
def search_results(request):
    query = request.GET.get('q')
    artists = Artist.objects.filter(artist_name__icontains=query)
    tracks = Track.objects.filter(track_name__icontains=query).order_by('-track_release_date')
    results = list(artists) + list(tracks)
    return render(request, 'music/search_results.html', {'results': results, 'query': query})


# 아티스트 페이지
def artist_page(request, artist_id):
    page = request.GET.get('page','1') # 페이지
    artist = Artist.objects.get(artist_id=artist_id)
    tracks = Track.objects.filter(artist_id=artist_id).order_by('-track_release_date')
    artistboards = ArtistBoard.objects.filter(artist_id=artist_id)
    paginator = Paginator(artistboards,5)
    page_obj = paginator.get_page(page)
    return render(request, 'music/artist_page.html', {'artist': artist, 'tracks' : tracks, 'artistboards': page_obj ,'boardcount' : paginator.count})


def track_page(request, track_id):
    page = request.GET.get('page','1') # 페이지
    track = Track.objects.get(track_id=track_id)
    similar_track_ids = [track.similar_track_id1, track.similar_track_id2, track.similar_track_id3,
                         track.similar_track_id4, track.similar_track_id5]
    similar_tracks = Track.objects.filter(track_id__in=similar_track_ids)
    trackboards = TrackBoard.objects.filter(track_id=track_id)

    paginator = Paginator(trackboards,5)
    page_obj = paginator.get_page(page)
    return render(request, 'music/track_page.html', {'track': track, 'similar_tracks': similar_tracks,'trackboards':page_obj,'boardcount' : paginator.count})


# 검색창 결과 - 가수, 음악
def playlist(request):
    tracklikes = request.user.like_track.all()
    playlists = []
    for tracklike in tracklikes:
        track = Track.objects.get(track_id=tracklike.track_id)
        playlists.append(track)
    return render(request, 'music/playlist.html', {'playlists': playlists})


def followlist(request):
    followlikes = request.user.like_artist.all()
    followlists = []
    for artistlike in followlikes:
        artist = Artist.objects.get(artist_id = artistlike.artist_id)
        followlists.append(artist)
    return render(request, 'music/follow.html', {'followlists': followlists})


def artist_review_create(request, artist_id):
    user = request.user
    if request.method == "POST":
        form = ArtistAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.artist_id = artist_id
            answer.user_id = user.id
            answer.username = user.username
            answer.save()
            return redirect("music:artist_page", artist_id=artist_id)
    else:
        form = ArtistAnswerForm()
    return render(request, 'music/artist_page.html', {'artist_id': artist_id, 'form': form})


def track_review_create(request, track_id):
    user = request.user
    if request.method == "POST":
        form = TrackAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.track_id = track_id
            answer.user_id = user.id
            answer.username = user.username
            answer.save()
            return redirect("music:track_page", track_id=track_id)
    else:
        form = TrackAnswerForm()
    return render(request, 'music/track_page.html', {'track_id': track_id, 'form': form})


def recent_reply(request):
    # 최근 게시물
    recent_artistboards = ArtistBoard.objects.order_by('-create_date')[:5]
    recent_trackboards = TrackBoard.objects.order_by('-create_date')[:5]
    context = {'recent_artistboards': recent_artistboards , 'recent_trackboards': recent_trackboards}
    return render(request, 'music/recent_comment.html', context)
