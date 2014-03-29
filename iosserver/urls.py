from django.conf.urls import patterns, include, url
from views import *
from django.contrib import admin
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iosserver.views.home', name='home'),
    # url(r'^iosserver/', include('iosserver.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^hello/$', hello),
    (r'^time/$',current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^books/', include('books.urls')),
    ('', include('contact.urls')),
    (r'^rating/', include('Rating.urls')),
    (r'^login/',include('login.urls')),
    (r'^money/',include('moneyManager.urls')),
    (r'^snippets/', include('snippets.urls')),
    (r'^',include('relations.urls')),
    #rest framework urls
    (r'^', include(router.urls)),
    (r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
