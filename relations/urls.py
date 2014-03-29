from django.conf.urls import patterns, include, url
from relations import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    url(r'^album/$', views.AlbumList.as_view(), name='album-list'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view(), name='album-detail'),
    url(r'^track/$', views.TrackList.as_view(), name='track-list'),
    url(r'^track/(?P<pk>[0-9]+)/$', views.TrackDetail.as_view(), name='track-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)