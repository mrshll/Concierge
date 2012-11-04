from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# register our api resources
from tastypie.api import Api
from recommendation_item.api import RestaurantResource
from user_profile.api import UserProfileResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(RestaurantResource())
v1_api.register(UserProfileResource())
v1_api.register(UserResource())


urlpatterns = patterns('concierge.views',
    url(r'', include('user_profile.urls')),
    url(r'^$', 'index', name='index'),

    # api routing
    (r'^api/', include(v1_api.urls)),

    # survey
    (r'^survey/', include('survey.urls')),

    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('recommendation_item.views',
    url(r'^getFactual/', 'testFactual'),
)
