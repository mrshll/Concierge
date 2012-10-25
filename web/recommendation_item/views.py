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

    for datum in query_data:
        print datum
        # dictionary to hold current item's descriptors
        sources = "{'factual':["+datum.get('factual_id', 0)+"]}"

        a, a_created = Address.objects.get_or_create(street_address=datum.get('address',0),
                                                               city=datum.get('locality',0),
                                                              state=datum.get('region',0),
                                                            zipcode=datum.get('postcode',0),
                                                          longitude=datum.get('longitude',0),
                                                           latitude=datum.get('latitude',0))

        r, r_created = Restaurant.objects.get_or_create(   cuisines=datum.get('cuisine',0),
                                                             rating=datum.get('rating',0),
                                                              price=datum.get('price',0),
                                                            address=a,
                                                       data_sources=sources)
        print(a)
        print(r)

def testFactual(request):
    getRestaurantDataFromFactual(CAMPUS_CENTER)
    return HttpResponse("done")
