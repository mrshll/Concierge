import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from factual import Factual
from factual.utils import circle

from recommendation_item.models import Restaurant, Address

FACTUAL_KEY    = "frBfryFdtbYqmlgHrMB7LeSYWCOefyS0fhkIQTpp"
FACTUAL_SECRET = "Qh25xjtI1XzsJ2CT7TohBArnSQKt3P3v8uyHZKpC"

CAMPUS_CENTER = circle(42.4019,  -71.1193, 500)

factual = Factual(FACTUAL_KEY, FACTUAL_SECRET)

# location is a circle around the location you want results from
def getRestaurantDataFromFactual(location):
    query = factual.table("restaurants")
    query = query.filters({"country":"US"})
    query = query.geo(location)
    query_data = query.data()

#    for datum in query_data:
#        # dictionary to hold current item's descriptors
#        restaurant_data = json.loads(datum)
#        sources = "{'factual':["+restaurant_data['factual_id']+"]}"
#
#        a = Address(street_address=restaurant_data['address'],
#                                    city=restaurant_data['locality'],
#                                   state=restaurant_data['region'],
#                                 zipcode=restaurant_data['postcode'],
#                               longitude=restaurant_data['longitude'],
#                                latitude=restaurant_data['latitude'])
#        a.save()
#
#        r = Restaurant(cuisines=restaurant_data['cuisine'],
#                         rating=restaurant_data['rating'],
#                          price=restaurant_data['price'],
#                        address=a,
#                   data_sources=sources)
#        r.save()
#        print(a)
#        print(r)

def testFactual(request):
    getRestaurantDataFromFactual(CAMPUS_CENTER)
    return HttpResponse("done")
