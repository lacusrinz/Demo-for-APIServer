from django.shortcuts import render
from relations.models import Album, Track
from relations.serializers import AlbumSerializer, TrackSerializer
from rest_framework import generics
# Create your views here.
class AlbumList(generics.ListCreateAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Album.objects.all()
	serializer_class = AlbumSerializer

class TrackList(generics.ListCreateAPIView):
	queryset = Track.objects.all()
	serializer_class = TrackSerializer

class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Track.objects.all()
	serializer_class = TrackSerializer