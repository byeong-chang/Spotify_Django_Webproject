from django.shortcuts import redirect
from rest_framework.response import Response

from .credentials import REDIRECT_URI,CLIENT_SECRET,CLIENT_ID
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from .util import update_or_create_user_tokens, is_spotify_authenticated

class AuthURL(APIView):
    def get(self, request, format=None):
        scopes = "user-read-playback-state user-modify-playback-state user-read-currently-playing"
        url = Request("GET","https://accounts.spotify.com/authorize",parama={
            'score' : scopes,
            'response_type' : 'code',
            'redirect_uri' : REDIRECT_URI,
            'client_id' : CLIENT_ID
        }).prepare().url
        return Response({'url': url}, status=status.HTTP_200_OK)

def spotify_callback(request, format=None):
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
    error = response.GET.get('error')

    if not request.session.exists(request.session.session_key):
        request.session.create()

    update_or_create_user_tokens(request.session.session_key, access_token,token_type,expires_in,refresh_token)
    return redirect('spotify:spotify_login')

class IsAuthenticated(APIView):
    def get(self, request, format=None):
        is_authenticate = is_spotify_authenticated(self.request.session.session_key)
        return Response({'status': is_authenticate}, status=status.HTTP_200_OK)


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # 사용자 인증
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # 로그인 처리
            login(request, user)
            return redirect('spotify:spotify_login')
        else:
            # 인증 실패 처리
            error_message = '유효한 로그인 정보를 입력해주세요.'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

