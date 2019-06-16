from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import *


class LoginResponseSerializer(serializers.Serializer):
    token = serializers.CharField(label=_("Token"))
    user_id = serializers.IntegerField(label=_("User_id"))
    email = serializers.CharField(label=_("email"))


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=False, read_only=True)
    band = BandSerializer(many=False, read_only=True)

    class Meta:
        model = Music
        fields = '__all__'


class PlaylistSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault()))
    owner_name = serializers.CharField(source='owner.username', read_only=True)
    musics = serializers.PrimaryKeyRelatedField(queryset=Music.objects, many=True)

    class Meta:
        model = Playlist
        fields = '__all__'

