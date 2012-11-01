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
  rr = RestaurantResource()
  # use learning algorithm to get restaurants sorted by recommendation percent
  all_restaurants = Restaurant.objects.all()
  all_users = User.objects.all()
  eng = RecommendationEngine(all_restaurants,all_users[0])
  sortedRestaurants = eng.sortRestaurants()

  return HttpResponse(str(sortedRestaurants[0].title))

