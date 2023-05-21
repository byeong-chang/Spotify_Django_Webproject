# 토큰 받아온 것 저장하는데 사용된다.
from requests import post, put, get

from music.models import User
from .models import spotifyToken
from django.utils import timezone
from datetime import timedelta
from .credentials import CLIENT_ID, CLIENT_SECRET

BASE_URL = "https://api.spotify.com/v1/me/"


def get_user_tokens(session_id):
    user_tokens = spotifyToken.objects.filter(user=session_id)
    if user_tokens.exists():
        return user_tokens[0]
    else:
        return None


def update_or_create_user_tokens(session_id, access_token, token_type, expires_in, refresh_token, RottenMellon_user_id):
    tokens = get_user_tokens(session_id)
    expires_in = timezone.now() + timedelta(seconds=expires_in)
    if tokens:
        tokens.access_token = access_token
        tokens.refresh_token = refresh_token
        tokens.expires_in = expires_in
        tokens.token_type = token_type
        tokens.RottenMellon_user_id = RottenMellon_user_id
        tokens.save(update_fields=['access_token', 'refresh_token', 'expires_in', 'token_type', "RottenMellon_user_id"])
    else:
        tokens = spotifyToken(user=session_id, access_token=access_token,
                              refresh_token=refresh_token, token_type=token_type, expires_in=expires_in,
                              RottenMellon_user_id=RottenMellon_user_id)

        User.objects.filter(id=RottenMellon_user_id).update(expires_in=expires_in)
        tokens.save()


def is_spotify_authenticated(session_id):
    tokens = get_user_tokens(session_id)
    if tokens:
        expiry = tokens.expires_in
        if expiry <= timezone.now():
            refresh_spotify_token(session_id)
        return True
    return False


def refresh_spotify_token(session_id):
    refresh_token = get_user_tokens(session_id).refresh_token
    response = post('http://accounts.spotify.com/api/tiken', data={
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    expires_in = response.get('expires_in')
    refresh_token = response.get('refresh_token')

    update_or_create_user_tokens(session_id, access_token, token_type, expires_in, refresh_token)


# session_id 는 로그인한 유저, endpoint는 spotify에서 실행할 노래를 뜻함
def execute_spotify_api_request(session_id, endpoint, post_=False, put_=False):
    tokens = get_user_tokens(session_id)
    headers = {'Content-Type': 'application/json',
               "Authorization": "Bearer " + tokens.access_token}
    if post_:
        post(BASE_URL + endpoint, headers=headers)
    if put_:
        put(BASE_URL + endpoint, headers=headers)

    response = get(BASE_URL + endpoint, {}, headers=headers)
    try:
        return response.json()
    except:
        return {"Error": "Issue with request"}
