from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

from singly import SinglyHelper
from models import UserProfile

from recommendation_item.models import Restaurant
from recommendation_item.api import RestaurantResource

from learn.engine import RecommendationEngine


def authenticate_redirect(request, service):
  url = SinglyHelper.get_authorize_url(service)
  return HttpResponseRedirect(url)

def authorize_callback(request):
  code = request.GET.get('code')
  content = SinglyHelper.get_access_token(code)
  user_profile = UserProfile.objects.get_or_create_user(content['account'], content['access_token'])
  if not request.user.is_authenticated():
    user = authenticate(username=user_profile.user.username, password='fakepassword')
    auth_login(request, user)
  return HttpResponseRedirect('/')

def get_recommendation(request):
  # use learning algorithm to get restaurants sorted by recommendation percent
  all_restaurants = Restaurant.objects.all()
  user_profile = request.user.get_profile()
  user_favorites = user_profile.favorites.all()
  user_favorites_restaurants = [f.restaurant for f in user_favorites]
  print('user favorites : ' + str(user_favorites_restaurants))

  rec_restaurants = [r for r in all_restaurants if r not in
                     user_favorites_restaurants]
  print(rec_restaurants)

  eng = RecommendationEngine(rec_restaurants, request.user)
  sortedRestaurants = eng.sortRestaurants()

  return HttpResponse(str(sortedRestaurants[0].title))

