from django.db import models
from user_profile.singly import *
from django.contrib.auth.models import User
import json

def fill_profile(user_profile, singly_id, access_token):
  discovery_endpoint = '/services/facebook'
  self_endpoint = '/services/facebook/self'
  page_likes_endpoint = '/services/facebook/page_likes?limit=1000'
  request = {'auth': 'true'}
  fb_discovery = Singly(access_token=access_token).make_request(discovery_endpoint, request=request)
  fb_self = Singly(access_token=access_token).make_request(self_endpoint, request=request)
  fb_page_likes = Singly(access_token=access_token).make_request(page_likes_endpoint, request=request)

  udata = unicode("data")
  fb_profile = {}
  fb_profile["location"] = fb_self[0][udata][unicode("location")]
  fb_profile["education"] =  fb_self[0][udata][unicode("education")]
  fb_profile["birth_date"] = fb_self[0][udata][unicode("birthday")]
  fb_profile["gender"] =  fb_self[0][udata][unicode("gender")]
  fb_profile["interested_in"] = fb_self[0][udata][unicode("interested_in")]
  fb_profile["languages"] = fb_self[0][udata][unicode("languages")]
  fb_profile["friend_count"] = fb_discovery[unicode("friends")]
  fb_profile["likes"] = []
  for i in fb_page_likes:
    like = [i[udata][unicode("name")],i[udata][unicode("category")]]
    fb_profile["likes"].append(like)

  return json.dumps(fb_profile)
