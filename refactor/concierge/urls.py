from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('concierge.views',
    (r'^admin/', include(admin.site.urls)),
    url(r'', include('user_profile.urls')),
    url(r'^$', 'index', name='index'),
    url('^findafriend.html$', 'suggest_user'),
)
