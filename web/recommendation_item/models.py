from django.db import models
from django.contrib.gis.db import models
from django.contrib.localflavor.us.models import USStateField

from utility import models

# zipcode object set up with a polygon field such that we can filter based on proximity
class Zipcode(models.Model):
    code = models.CharField(max_length=5)
    poly = models.PolygonField()
    objects = models.GeoManager()

# address model from: https://docs.djangoproject.com/en/dev/ref/contrib/gis/model-api/
class Address(models.Model):
    num = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = USStateField()
    zipcode = Zipcode()
    objects = models.GeoManager()

class Restaurant(models.Model):
    cuisines = models.TextField(null=True, blank=True)

    # rating, dangerous assumption that this is always out of 5
    rating   = models.FloatField(null=True, blank=True)

    # price from 1-5
    price    = models.IntegerField(null=True, blank=True)


# a recommendation item abstracts the item being recommended. And example of a
# recommendation item is a restaurant, an event, or a song.
#
# Important features of a recommendation item (LIVE LIST)
#   - Has one or more data sources to get information from
#   - Has an address that can be filtered based on proximity to a location
class RecommendationItem(models.Model):
    date_added = models.DateTimeField(auto_now=True)
    data_sources = models.TextField(null=True, blank=True)
    address = models.ForeignKey(Address)


