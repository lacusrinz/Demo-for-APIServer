from django.conf.urls import patterns, include, url
from views import login, register

urlpatterns = patterns('',
	(r'^login/$', login),
	(r'^register/$',register),
)