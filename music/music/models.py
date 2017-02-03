from django.db import models

class Genre(models.Model):
    '''
    The genre Model contains the essential fields and behaviors of the genre table.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Nate Baker
    '''
    genre_name = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return '{0}'.format(self.genre_name)

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
