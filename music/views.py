from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.models import Album, Song
from.serializer import AlbumSerializer, SongSerializer


class AlbumList(APIView):
    def get(self, request):
        albums = Album.objects.all()
        selializer = AlbumSerializer(albums, many=True)
        return Response(selializer.data)

class SongList(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)