from music.music.models import *
from music.music.serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import *

class GenreViewSet(viewsets.ModelViewSet):
    ''' This class is a view that lists out all the genres when you click genres from the root, and then details about a genre if you click one from the genres list. Only admins have access to this view.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specific data from the API.

    Author: Nate Baker
    '''
    permission_classes = (IsAdminUser,)
    queryset = genre_model.Genre.objects.all()
    serializer_class = genre_serializer.GenreSerializer