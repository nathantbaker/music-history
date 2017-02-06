from music.music.models import *
from music.music.serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import *

class ArtistViewSet(viewsets.ModelViewSet):
    ''' This class is a view that lists out all the artists when you click artists from the root, and then details about an artist if you click one from the artists list. Only admins have access to this view.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specific data from the API.

    Author: Nate Baker
    '''
    permission_classes = (IsAdminUser,)
    queryset = artist_model.Artist.objects.all()
    serializer_class = artist_serializer.ArtistSerializer