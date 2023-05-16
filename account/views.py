from django.shortcuts import render, redirect
from account.forms import UserForm
from django.contrib.auth import authenticate, login
from music.models import User


# Create your views here.
def home(request):
    return render(request, 'account/home.html')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            row_password = form.cleaned_data.get("password1")
            # 사용자 인증 담당 : 아이디와 비밀번호가 DB랑 같은지 비교
            user = authenticate(username=username, password=row_password)
            # 로그인 담당 : 사용자에게 입력받은 request와 인증기록인 user를 통해 로그인 허용 또는 거부
            login(request, user)
            return redirect("music:search")
    else:  # Get 요청일 때
        form = UserForm()
    return render(request, "account/signup.html", {"form": form})


def spotifylink(request):
    AUTH_URL = "https://accounts.spotify.com/authorize?client_id=e65b8272f8c74edaa390da64883a2d93&response_type=code&redirect_uri=http://127.0.0.1:8000/social/complete/spotify/&scope=user-read-private%20user-read-email%20ugc-image-upload%20playlist-read-private%20playlist-modify-private%20playlist-modify-public%20user-read-recently-played%20user-top-read%20user-library-modify%20user-library-read"
    return redirect(AUTH_URL)