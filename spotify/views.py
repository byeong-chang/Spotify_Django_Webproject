from django.shortcuts import redirect, render
from django.utils import timezone
from rest_framework.response import Response

from music.models import User
from .credentials import REDIRECT_URI,CLIENT_SECRET,CLIENT_ID
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from .util import *

class AuthURL(APIView):
    def get(self, request, format=None):
        scopes = "user-read-playback-state user-modify-playback-state user-read-currently-playing"
        url = Request("GET","https://accounts.spotify.com/authorize",params={
            'score' : scopes,
            'response_type' : 'code',
            'redirect_uri' : REDIRECT_URI,
            'client_id' : CLIENT_ID
        }).prepare().url
        print(url)
        return redirect(url)


def spotify_callback(request, format=None):
    user = request.user
    code = request.GET.get('code')
    error = request.GET.get('error')

    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code' : code,
        'redirect_uri' : REDIRECT_URI,
        'client_id' : CLIENT_ID,
        'client_secret' : CLIENT_SECRET
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = request.GET.get('error')
    RottenMellon_user_id =user.id

    if not request.session.exists(request.session.session_key):
        request.session.create()

    update_or_create_user_tokens(request.session.session_key, access_token,token_type,expires_in,refresh_token,RottenMellon_user_id)
    return redirect('spotify:is_authenticated')

def IsAuthenticated(request):
    is_authenticate = is_spotify_authenticated(request.session.session_key)
    current_time = timezone.now()
    expires_in = request.user.expires_in
    # 두 datetime 객체 사이의 시간 간격 계산
    time_difference = expires_in - current_time
    seconds = time_difference.total_seconds()
    return render(request, 'music/search.html', {'is_authenticate' : is_authenticate, "time_diff" : seconds})

class CurrentSong(APIView):
    def get(self, request, format = None):
        # room_code =  self.request.session.get("room_code")
        # room = Room.objects.filter(code=room_code)
        # if room.exists():
        #     room = room[0]
        # else:
        #     return Response({},status=status.HTTP_404_NOT_FOUND)
        # host = room.host
        host = self.request.COOKIES.get('sessionid')
        if host.exists():
            endpoint = 'player/currently-playing'
        else:
            return Response({},status=status.HTTP_404_NOT_FOUND)

        response = execute_spotify_api_request(host, endpoint)

        # if 'error' in response or 'item' not in response:
        #     return Response({},status=status.HTTP_204_NO_CONTENT)

        # item = response.get('item')
        # duration = item.get('duration_ms')
        # progress = response.get("progress_ms")
        # album_cover = item.get('album').get('images')[0].get('url')
        # is_playing = response.get('is_playing')
        # song_id = item.get('id')
        #
        # artist_string = ""
        #
        # for i,artist in enumerate(item.get('artist')):
        #     if i>0:
        #         artist_string +=", "
        #     name = artist.get("name")
        #     artist_string += name
        #
        # song = {
        #     'title' : item.get('name'),
        #     'artist' : artist_string,
        #     'duration' : duration,
        #     'time' : progress,
        #     'image_url' : album_cover,
        #     'is_playing' : is_playing,
        #     'votes' : 0,
        #     'id' : song_id
        # }

        return Response(response,status=status.HTTP_200_OK)

