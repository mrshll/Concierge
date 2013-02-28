from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

from singly import SinglyHelper
from models import UserProfile
from utility import fb_utility

def authenticate_redirect(request, service):
  url = SinglyHelper.get_authorize_url(service)
  return HttpResponseRedirect(url)

def authorize_callback(request):
  code = request.GET.get('code')
  content = SinglyHelper.get_access_token(code)
  user_profile = UserProfile.objects.get_or_create_user(content['account'], content['access_token'])
  user_profile.fb_data = fb_utility.fill_profile(user_profile, content['account'], content['access_token'])
  user_profile.save()
  if not request.user.is_authenticated():
    user = authenticate(username=user_profile.user.username, password='fakepassword')
    auth_login(request, user)
  return HttpResponseRedirect('/')

