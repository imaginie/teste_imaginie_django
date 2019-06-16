# -*- coding: utf-8 -*-

from django.conf.urls import (url)
from rest_framework import routers

from .views import *

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'playlists', PlaylistViewSet,base_name="playlists")
urlpatterns = [
    url(r'^auth$', CustomAuthToken.as_view({'post': 'login', 'get': 'logout'}), name='obtain_token'),
    url('^playlists/search$',
        SearchViewSet.as_view({'get': 'playlist'}), name='search-list'),
    url('^playlists/(?P<id_in>\d+)/add/(?P<id_out>\d+)$',
        CustomViewSet.as_view({'post': 'add'}), name='playlist-detail'),
    url('^playlists/(?P<id>\d+)/musics$',
        MusicViewSet.as_view({'get': 'list'}), name='music-list'),
    url('^playlists/(?P<id>\d+)/musics/search$',
        SearchViewSet.as_view({'get': 'music'}), name='search-list'),
]
urlpatterns += router.urls
