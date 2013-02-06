from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
import simplejson

# from survey.forms import UserSurvey
# from user_profile.models import Favorite


def index(request, template='index.html'):
    services = [
        'Facebook',
        'foursquare',
        'Instagram',
        'Tumblr',
        'Twitter',
        'LinkedIn',
        'FitBit',
        'Email'
    ]
    if request.user.is_authenticated():
        print(request.user)
        user_profile = request.user.get_profile()
        # user_favorites = user_profile.favorites.all()
        # user_favorites_restaurants = [f.restaurant for f in user_favorites]
        print(user_profile.profiles)
        # if request.method == "POST":
          # form = UserSurvey(request.POST)
          # if form.is_valid():
          #   # process data
          #   favorites = form.cleaned_data['favorites']
          #   for r in favorites:
          #     if r not in user_favorites_restaurants:
          #       f = Favorite(restaurant=r)
          #       f.save()
          #       user_profile.favorites.add(f)
          #   user_profile.save()
          #   return HttpResponseRedirect("/")
        # else:
          # form = UserSurvey()

        if user_profile.profiles and user_profile.profiles != "":
          # We replace single quotes with double quotes b/c of python's strict json requirements
          profiles = simplejson.loads(user_profile.profiles.replace("'", '"'))
        else:
          profiles = ""
    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response
