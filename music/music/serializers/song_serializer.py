from rest_framework import serializers
from music.music.models import *

class SongSerializer(serializers.HyperlinkedModelSerializer):
    ''' This class translates the Song model into other formats, in this case JSON by default.

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.

    Author: Nate Baker
    '''
    class Meta:
        ''' This method is tied to the ProductsSerializer class and tells the serializer to serialize all fields in the table.
        '''
        model = song_model.Song
        fields = '__all__'