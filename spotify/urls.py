from django.urls import path
from . import views

app_name = "spotify"

urlpatterns = [
    path('get-auth-url/', views.AuthURL.as_view(), name='spotify_login'),
    path('redirect/',views.spotify_callback, name="redirect_login"),
    path('is-authenticated/', views.IsAuthenticated, name="is_authenticated"),
    path('current-song',views.CurrentSong.as_view()),
]