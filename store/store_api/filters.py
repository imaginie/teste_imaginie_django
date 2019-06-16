import django_filters as filters
from .models import *


# Create your views here.

class PlaylistFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    musics__name = filters.CharFilter(lookup_expr='icontains')
    musics__band__name = filters.CharFilter(lookup_expr='icontains')
    musics__genre__name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Playlist
        fields = {'name', 'musics__name', 'musics__band__name', 'musics__genre__name'}


class MusicFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    band__name = filters.CharFilter(lookup_expr='icontains')
    genre__name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Music
        fields = {'name', 'band__name', 'genre__name'}
