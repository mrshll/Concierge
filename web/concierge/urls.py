from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('concierge.views',
    url(r'', include('singly.urls')),
    url(r'^$', 'index', name='index'),


    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('recommendation_item.views',
    url(r'^getFactual/', 'testFactual'),
)
