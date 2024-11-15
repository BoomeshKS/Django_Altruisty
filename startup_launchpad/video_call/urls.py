from django.urls import path
from . import views

urlpatterns = [
    path("video_call/", views.lobby, name="lobby"),
    path("room/", views.room, name='room'),
    path("main/", views.main, name='main')
]