from django.conf.urls import patterns, include, url
from views import getall, search, postsearch

urlpatterns = patterns('',
	(r'^all/$', getall),
	(r'^search', search),
	(r'^player',postsearch),
)