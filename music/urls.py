from django.urls import path
from . import views

app_name = "music"

urlpatterns = [
    path('', views.search, name='music_home'),
    path('search/', views.search, name='search'),
    path('search_results/', views.search_results, name='search_results'),
    path('playlist/', views.playlist, name="playlist"),
    path('followlist/', views.followlist, name="followlist"),
    path('recent_reply/', views.recent_reply, name='recent_reply'),

    path('artist/<str:artist_id>/', views.artist_page, name='artist_page'),
    path('track/<str:track_id>/', views.track_page, name='track_page'),
    path('artist/review_create/<str:artist_id>/', views.artist_review_create, name="artist_review_create"),
    path('track/review_create/<str:track_id>/', views.track_review_create, name="track_review_create"),
]