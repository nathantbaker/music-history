from music.music.models import *
from music.music.serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import *

class AlbumViewSet(viewsets.ModelViewSet):
    ''' This class is a view that lists out all the album when you click album from the root, and then details about an album if you click one from the album list. Only admins have access to this view.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specific data from the API.

    Author: Nate Baker
    '''
    permission_classes = (IsAdminUser,)
    queryset = album_model.Album.objects.all()
    serializer_class = album_serializer.AlbumSerializer