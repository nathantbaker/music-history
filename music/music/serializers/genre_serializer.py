from rest_framework import serializers
from music.music.models import *


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    ''' This class translates the Genre model into other formats, in this case JSON by default.

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.

    Author: Nate Baker
    '''
    class Meta:
        ''' This method is tied to the GenreSerializer class and tells the serializer to serialize all fields in the table.
        '''
        model = genre_model.Genre
        fields = '__all__'