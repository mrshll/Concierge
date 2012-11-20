from time import sleep

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from factual import Factual
from factual.utils import circle

from recommendation_item.models import Restaurant, Address

FACTUAL_KEY    = "frBfryFdtbYqmlgHrMB7LeSYWCOefyS0fhkIQTpp"
FACTUAL_SECRET = "Qh25xjtI1XzsJ2CT7TohBArnSQKt3P3v8uyHZKpC"


factual = Factual(FACTUAL_KEY, FACTUAL_SECRET)

# location is a circle around the location you want results from
def getRestaurantDataFromFactual(location):
  added_names = []

  query = factual.table("restaurants")
  query = query.filters({"country":"US"})
  query = query.geo(location)

  query_data = query.data()
  print(len(query_data))

  for datum in query_data:
    print (datum.get('name', 'No name given'))
    print(datum.get('cuisine',"No cuisine given"))
    # dictionary to hold current item's descriptors
    sources = "{'factual':["+datum.get('factual_id', 0)+"]}"

    a, a_created = Address.objects.get_or_create(street_address=datum.get('address',None),
                                                           city=datum.get('locality',None),
                                                          state=datum.get('region',None),
                                                        zipcode=datum.get('postcode',None),
                                                      longitude=datum.get('longitude',None),
                                                       latitude=datum.get('latitude',None))

    r, r_created = Restaurant.objects.get_or_create(      title=datum.get('name',None),
                                                       cuisines=datum.get('cuisine',None),
                                                         rating=datum.get('rating', -1),
                                                          price=datum.get('price', -1),
                                                        address=a,
                                                   data_sources=sources)
    if r_created:
      added_names.append(datum.get('name',None))

  return str(added_names)

def testFactual(request):
  LENGTH_OF_ONE_LAT = 111081.59847784671
  LENGTH_OF_ONE_LON = 82291.40843937476
  lat = 42.418837
  lon = -71.130553
  end_lat = 42.33
  end_lon = -71.033440

  while lat >= end_lat:
    while lon <= end_lon:
      print(str(lat) + "," + str(lon))
      LOC = circle(lat, lon, 100)
      getRestaurantDataFromFactual(LOC)
      lon += (100/LENGTH_OF_ONE_LON)
      sleep(1)
    lat -= (100/LENGTH_OF_ONE_LAT)
    lon = -71.130553
  return HttpResponse("OK")

