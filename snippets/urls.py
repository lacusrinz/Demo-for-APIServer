from django.conf.urls import patterns, include, url
# from views import snippet_list, snippet_detail
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = patterns('snippets.views',
    url(r'^list/$', views.SnippetList.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),  
)

urlpatterns = format_suffix_patterns(urlpatterns)