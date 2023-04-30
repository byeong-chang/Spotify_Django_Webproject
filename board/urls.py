from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path('artist/board/<int:artist_board_id>/', views.artist_vote, name='artist_vote'),
    path('track/board/<int:track_board_id>/', views.track_vote, name='track_vote'),
    path('artsit/follow/<str:artist_id>/', views.artist_follow, name='artist_follow'),
    path('track/follow/<str:track_id>/', views.track_follow, name='track_follow'),
]