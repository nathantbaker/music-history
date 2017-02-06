class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    ''' This class translates the Artist model into other formats, in this case JSON by default.

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.

    Author: Nate Baker
    '''
    class Meta:
        ''' This method is tied to the ArtistSerializer class and tells the serializer to serialize all fields in the table.
        '''
        model = Artist
        fields = '__all__'


class SongSerializer(serializers.HyperlinkedModelSerializer):
    ''' This class translates the Song model into other formats, in this case JSON by default.

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.

    Author: Nate Baker
    '''
    class Meta:
        ''' This method is tied to the ProductsSerializer class and tells the serializer to serialize all fields in the table.
        '''
        model = Song
        fields = '__all__'


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    ''' This class translates the Album model into other formats, in this case JSON by default.

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.

    Author: Nate Baker
    '''
    class Meta:
        ''' This method is tied to the AlbumSerializer class and tells the serializer to serialize all fields in the table.
        '''
        model = Album
        fields = '__all__'


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    ''' This class translates the Genre model into other formats, in this case JSON by default.

    Argument List:
    -serializers.HyperlinkedModelSerializer: This argument allows the class to access field types.

    Author: Nate Baker
    '''
    class Meta:
        ''' This method is tied to the GenreSerializer class and tells the serializer to serialize all fields in the table.
        '''
        model = Genre
        fields = '__all__'