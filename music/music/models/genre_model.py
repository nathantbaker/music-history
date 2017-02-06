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