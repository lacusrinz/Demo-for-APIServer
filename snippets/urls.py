from django.conf.urls import patterns, include, url
# from views import snippet_list, snippet_detail
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = patterns('snippets.views',
	url(r'^$', 'api_root'),
    url(r'^list/$', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),  
    url(r'^detail/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
)

urlpatterns = format_suffix_patterns(urlpatterns)