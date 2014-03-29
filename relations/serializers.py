from rest_framework import serializers
from relations.models import Album, Track
import time

class TrackListingField(serializers.RelatedField):
	def to_native(self, value):
		duration = time.strftime('%M:%S', time.gmtime(value.duration))
		return 'Track %d: %s (%s)' %(value.order,value.title,duration)

# class TrackHyperlinkedField(serializers.HyperlinkedRelatedField):
#     def get_url(self, obj, view_name, request, format):
#         kwargs = {'album': obj.album, 'order': obj.order}
#         return reverse(view_name, kwargs=kwargs, request=request, format=format)

#     def get_object(self, queryset, view_name, view_args, view_kwargs):
#         account = view_kwargs['album']
#         slug = view_kwargs['order']
#         return queryset.get(album=album, order=order)

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
#	tracks = serializers.RelatedField(many=True)
#	tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#	tracks = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='track-detail')
#	track_listing = serializers.HyperlinkedIdentityField(view_name='track-list')
	tracks = TrackListingField(many=True)
#	tracks = TrackHyperlinkedField(many=True)
	
	class Meta:
		model = Album
		fields = ('id','url','aubum_name', 'artist', 'tracks')

class TrackSerializer(serializers.ModelSerializer):
	albumname = serializers.Field(source='album.aubum_name')
	class Meta:
		model = Track
		fields = ('id','album','albumname', 'order', 'title', 'duration')