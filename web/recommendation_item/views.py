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
  print location
  query = factual.table("restaurants")
  query = query.filters({"country":"US"})
  query = query.geo(location)
  print(query.get_url())

  query_data = query.data()

  added_names = []

  for datum in query_data:
    print (datum.get('name',0))
    # dictionary to hold current item's descriptors
    sources = "{'factual':["+datum.get('factual_id', 0)+"]}"

    a, a_created = Address.objects.get_or_create(street_address=datum.get('address',0),
                                                           city=datum.get('locality',0),
                                                          state=datum.get('region',0),
                                                        zipcode=datum.get('postcode',0),
                                                      longitude=datum.get('longitude',0),
                                                       latitude=datum.get('latitude',0))

    r, r_created = Restaurant.objects.get_or_create(      title=datum.get('name',0),
                                                       cuisines=datum.get('cuisine',0),
                                                         rating=datum.get('rating',0),
                                                          price=datum.get('price',0),
                                                        address=a,
                                                   data_sources=sources)
    if r_created:
      added_names.append(datum.get('name',0))

    return str(added_names)

def testFactual(request):
  CAMPUS_CENTER = circle(42.4019,  -71.1193, 5000)
  return HttpResponse(getRestaurantDataFromFactual(CAMPUS_CENTER))

