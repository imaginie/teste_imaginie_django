from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import (viewsets)
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.status import (
    HTTP_404_NOT_FOUND,
    HTTP_304_NOT_MODIFIED,
    HTTP_200_OK,
)

from .permissions import *
from .filters import *
from .serializers import *


# @csrf_exempt
class CustomAuthToken(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer
    permission_classes_by_action = {'login': [AllowAny],
                                    'default': [IsAuthenticated]}

    def get_permissions(self):
        try:
            # return permission_classes depending on 'action'
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes_by_action['default']]

    @swagger_auto_schema(operation_id='login', request_body=AuthTokenSerializer,
                         responses={200: LoginResponseSerializer})
    def login(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        Token.objects.get_or_create(user=user)
        return Response({
            'token': 'Token ' + user.auth_token.key,
            'user_id': user.pk,
            'email': user.email
        })

    @swagger_auto_schema(operation_id='logout')
    def logout(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        return Response({"success": _("Successfully logged out.")},
                        status=HTTP_200_OK)


class CustomViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated ,IsOwnerOrAdminOrReadOnly)

    @swagger_auto_schema(request_body=None, responses={200: PlaylistSerializer})
    def add(self, request, *args, **kwargs):
        queryset = Playlist.objects
        queryset_in = queryset.filter(id=kwargs["id_in"])
        if not queryset_in.exists():
            return Response(["Playlist: " + kwargs["id_in"]], status=HTTP_404_NOT_FOUND)
        queryset_out = queryset.filter(id=kwargs["id_out"])
        if not queryset_out.exists():
            return Response(["Playlist: " + kwargs["id_out"]], status=HTTP_404_NOT_FOUND)
        if not queryset_out.get().musics.exclude(id__in=queryset_in.values('musics')).exists():
            return Response(status=HTTP_304_NOT_MODIFIED)
        playlist = queryset_in.get()
        self.check_object_permissions(request, playlist)
        for music in queryset_out.get().musics.all():
            playlist.musics.add(music)
        playlist.save()
        serializer = PlaylistSerializer(playlist, many=False)
        return Response(data=serializer.data)


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects
    serializer_class = PlaylistSerializer
    filter_class = PlaylistFilter
    permission_classes = (IsAuthenticated , IsOwnerOrAdminOrReadOnly)


class MusicViewSet(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    filter_class = MusicFilter
    permission_classes = (IsAuthenticated ,IsOwnerOrAdminOrReadOnly)

    def list(self, request, *args, **kwargs):
        f = self.filter_class(request.GET, queryset=Playlist.objects.get(id=kwargs["id"]).musics)
        queryset = f.qs
        if not queryset.exists():
            return Response([], status=HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data)


class SearchViewSet(viewsets.ViewSet):
    @swagger_auto_schema(operation_id='playlists_search')
    def playlist(self, request, *args, **kwargs):
        return Response(data={"Search Fields": PlaylistFilter().Meta.fields})

    @swagger_auto_schema(operation_id='playlists_musics_search')
    def music(self, request, id=None):
        return Response(data={"Search Fields": MusicFilter.Meta.fields})
