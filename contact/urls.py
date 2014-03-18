from django.conf.urls import patterns, include, url
from views import contact

urlpatterns = patterns("",
	(r'^contact/$', contact),
)