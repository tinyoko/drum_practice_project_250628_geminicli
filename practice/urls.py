from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('upload/', views.upload_song, name='upload_song'),
    path('practice/<int:song_id>/', views.practice_view, name='practice_view'),
    path('score/<int:score_id>/save_timings/', views.save_timings, name='save_timings'),
]
