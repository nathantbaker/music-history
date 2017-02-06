from django.db import models
from .genre_model import *

class Artist(models.Model):
    '''
    The Artists Model contains the essential fields and behaviors of the Artists table.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Nate Baker
    '''
    artist_name = models.CharField(max_length=200, blank=True, default='')
    genre = models.ForeignKey(Genre, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.artist_name)