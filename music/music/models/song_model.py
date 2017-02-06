from django.db import models
from .artist_model import *
from .album_model import *

class Song(models.Model):
    '''
    The Song Model contains the essential fields and behaviors of the Song table.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Nate Baker
    '''
    song_name = models.CharField(max_length=200, blank=True, default='')
    song_length = models.IntegerField()
    artist = models.ForeignKey(Artist, null=True, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.song_name)