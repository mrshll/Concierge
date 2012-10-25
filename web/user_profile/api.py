from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

from user_profile.models import UserProfile

class UserProfileResource(ModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'user_profile'

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        filtering = {
            'username': ALL,
            }