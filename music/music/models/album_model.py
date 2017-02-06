from django.db import models
from .artist_model import *

class Album(models.Model):
    '''
    The album Model contains the essential fields and behaviors of the album table.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Nate Baker
    '''
    album_name = models.CharField(max_length=200, blank=True, default='')
    artist = models.ForeignKey(Artist, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.album_name)