from rest_framework import serializers
from music.models import *

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    ''' The ArtistSerializer class translates the Artists models into other formats, in this case JSON by default. that Products table so a database can be created from it.

    Method List:
    -Meta
    -create
    -update

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.

    Author: Nate Baker, Python Ponies
    '''
    class Meta:
        ''' This method is tied to the ProductsSerializer class and tells the serializer to serialize all fields in the table.
        '''
        model = Artists
        fields = '__all__'
