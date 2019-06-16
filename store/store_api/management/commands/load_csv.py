from django.core.management.base import BaseCommand
from django import apps
import csv
from store_api.models import *


class Command(BaseCommand):
    help = 'Creating model objects according the file load.csv'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('store_api/fixtures/load.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='|')
            line_count = 0
            for row in reader:
                if line_count == 0:
                    header = row
                    line_count += 1
                else:
                    _object_dict = {key: value for key, value in zip(header, row)}
                    genre = Genre.objects.update_or_create(name=_object_dict.pop("genre"))[0]

                    band = Band.objects.update_or_create(name=_object_dict.pop("band"))[0]

                    music = Music.objects.update_or_create(name=_object_dict.pop("music_name"), genre=genre, band=band)[0]

                    playlist = Playlist.objects.update_or_create(name=_object_dict.pop("playlist"))[0]
                    playlist.musics.add(music)

                    line_count += 1
