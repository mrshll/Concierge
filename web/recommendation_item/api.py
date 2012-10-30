from tastypie.resources import ModelResource
from recommendation_item.models import Restaurant

class RestaurantResource(ModelResource):
    class Meta:
        queryset = Restaurant.objects.all()
        resource_name = 'restaurant'
