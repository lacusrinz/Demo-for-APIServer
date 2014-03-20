from django.conf.urls import patterns, include, url
# from views import snippet_list, snippet_detail
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

# urlpatterns = patterns('snippets.views',
# 	url(r'^$', 'api_root'),
#     url(r'^list/$', views.SnippetList.as_view(), name='snippet-list'),
#     url(r'^detail/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
#     url(r'^users/$', views.UserList.as_view(), name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),  
#     url(r'^detail/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
# )

# urlpatterns = format_suffix_patterns(urlpatterns)

from snippets.views import SnippetViewSet, UserViewSet
from rest_framework import renderers

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns(patterns('snippets.views',
    url(r'^$', 'api_root'),
    url(r'^detail/$', snippet_list, name='snippet-list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    url(r'^detail/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
))