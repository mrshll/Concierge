from django.template.context import RequestContext

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render

from survey.forms import UserSurvey
from user_profile.models import Favorite

def favorites(request):
  if request.method == "POST":
    form = UserSurvey(request.POST)
    if form.is_valid():
      # process data
      user_profile = request.user.get_profile()
      user_favs = [ f.restaurant for f in user_profile.favorites.all() ]
      favorites = form.cleaned_data['favorites']
      for r in favorites:
        if r not in user_favs:
          f = Favorite(restaurant=r)
          f.save()
          user_profile.favorites.add(f)
      return HttpResponseRedirect("/")
  else:
    form = UserSurvey()
  return render(request, "favorites.html", { "form" : form })
