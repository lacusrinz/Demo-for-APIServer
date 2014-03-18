from django.conf.urls import patterns, include, url
from views import search, search_form

urlpatterns = patterns('',
	(r'^search-form/$', search_form),
	(r'^search/$', search),
)