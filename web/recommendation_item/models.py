import math
from django.db import models
from django.contrib.gis.db import models as geo_models
from django.contrib.localflavor.us.models import USStateField

from django.contrib.auth.models import User

from utility import models as util_models

# address model from: https://docs.djangoproject.com/en/dev/ref/contrib/gis/model-api/
class Address(geo_models.Model):
  longitude = models.FloatField()
  latitude = models.FloatField()
  street_address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = USStateField()
  zipcode = models.CharField(max_length=10)
  objects = geo_models.GeoManager()

# holds a set of recommendation_items and their ratings for a particular user
class RecommenationList(models.Model):
  user = models.ForeignKey(User)

# a recommendation item abstracts the item being recommended. And example of a
# recommendation item is a restaurant, an event, or a song.
#
# Important features of a recommendation item (LIVE LIST)
#   - Has one or more data sources to get information from
#   - Has an address that can be filtered based on proximity to a location
class RecommendationItem(models.Model):
  recommendation_list = models.ManyToManyField(RecommendationList)
  date_added = models.DateTimeField(auto_now=True)
  data_sources = models.TextField(null=True, blank=True)
  address = models.ForeignKey(Address)
  title = models.CharField(max_length=120, default="")

    # takes in a destination and returns the distance from it in miles
    def distanceFrom(self, dest):
      lat1 = self.address.latitude
      lon1 = self.address.longitude
      lat2 = dest.address.latitude
      lon2 = dest.address.longitude
      radius = 6371 # km of earth

      dlat = math.radians(lat2-lat1)
      dlon = math.radians(lon2-lon1)
      a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1))\
          * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
      c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
      d = radius * c

      # convert to miles
      d = d * 0.621371

      return d

# specific recommendation item extensions
class Restaurant(RecommendationItem):
  cuisines = models.TextField(null=True, blank=True)
  # rating, dangerous assumption that this is always out of 5
  rating   = models.FloatField(null=True, blank=True)
  # price from 1-5
  price    = util_models.IntegerRangeField(min_value=1,max_value=5)

