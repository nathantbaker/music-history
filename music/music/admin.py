from django.contrib import admin
from music.music.models import *

admin.site.register(artist_model.Artist)
admin.site.register(song_model.Song)
admin.site.register(album_model.Album)
admin.site.register(genre_model.Genre)