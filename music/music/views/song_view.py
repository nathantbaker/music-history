from music.music.models import *
from music.music.serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import *

class SongViewSet(viewsets.ModelViewSet):
    ''' This class is a view that lists out all the songs when you click songs from the root, and then details about a song if you click one from the songs list. Only admins have access to this view.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specific data from the API.

    Author: Nate Baker
    '''
    permission_classes = (IsAdminUser,)
    queryset = song_model.Song.objects.all()
    serializer_class = song_serializer.SongSerializer