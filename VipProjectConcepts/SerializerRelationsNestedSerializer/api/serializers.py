
from rest_framework import serializers
from .models import Song,Singer

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']


# class SingerSerializer(serializers.ModelSerializer):
#
#     #song = serializers.StringRelatedField(many=True, read_only=True)    # --> it will give the songs sung by the singer
#     #song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
#                                             # it will create hyperlink and on clicking it will open the details of that song
#     class Meta:
#         model = Singer
#         #fields = ['id','name','gender','song']  # song-->related name of song in models.py


# by nested serializer-->
class SingerSerializer(serializers.ModelSerializer):
    song = SongSerializer(many=True,read_only=True)     # it has to be related name from models.py file i.e. song
                                                        # else it will not work
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']        #-->  it will give nesting into the api i.e. which songs sung by that singer


