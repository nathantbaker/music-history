from django.db import models

# Create your models here.

class Artists(models.Model):
    '''
    The Artists Model contains the essential fields and behaviors of Artists Data.

    Argument List:
        -models.Model: This argument allows the class to access field types.

    Author: Nate Baker, Python Ponies
    '''
    artist_name = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return '{0}'.format(self.artist_name)