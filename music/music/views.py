from music.models import *
from music.serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import *

class ArtistsViewSet(viewsets.ModelViewSet):
    ''' The ProductsViewSet class is a view that lists out all products and details about a product.

    Argument List:
        -generics.ModelViewSet: This method returns both a collect of data and specifi data from the API.

    Author: Nathan Baker, Python Ponies
    '''
    permission_classes = (IsAdminUser,)
    queryset = Artists.objects.all()
    serializer_class = ArtistSerializer