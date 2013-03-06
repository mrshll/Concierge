from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
import simplejson
from learn.Collab import Collab

def index(request, template='index.html'):
    services = [
        'Facebook',
        'Foursquare',
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
        print(user_profile.profiles)
        if user_profile.profiles and user_profile.profiles != "":
          # We replace single quotes with double quotes b/c of python's strict json requirements
          profiles = simplejson.loads(user_profile.profiles.replace("'", '"'))
        else:
          profiles = ""
    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response

def suggest_user(request):
    template = 'findafriend.html' # put a template here
    if request.user.is_authenticated():
      user_profile = request.user.get_profile()
      suggested_user = Collab().suggest_users(user_profile, 1)[0].user
      return render_to_response(template, locals(), context_instance=RequestContext(request))
    return HttpResponseRedirect(reverse('concierge.views.index'))
