# coding=utf-8

from __future__ import unicode_literals
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = u'Genre'
        verbose_name_plural = u'Genres'

    def __str__(self):
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = u'Band'
        verbose_name_plural = u'Bands'

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = u'Music'
        verbose_name_plural = u'Musics'

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = u'Playlist'
        verbose_name_plural = u'Playlists'

    def __str__(self):
        return self.name
