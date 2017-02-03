from .models import *
from .serializers import *
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
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongViewSet(viewsets.ModelViewSet):
    ''' This class is a view that lists out all the songs when you click songs from the root, and then details about a song if you click one from the songs list. Only admins have access to this view.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specific data from the API.

    Author: Nate Baker
    '''
    permission_classes = (IsAdminUser,)
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    ''' This class is a view that lists out all the album when you click album from the root, and then details about an album if you click one from the album list. Only admins have access to this view.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specific data from the API.

    Author: Nate Baker
    '''
    permission_classes = (IsAdminUser,)
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class GenreViewSet(viewsets.ModelViewSet):
    ''' This class is a view that lists out all the genres when you click genres from the root, and then details about a genre if you click one from the genres list. Only admins have access to this view.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specific data from the API.

    Author: Nate Baker
    '''
    permission_classes = (IsAdminUser,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer