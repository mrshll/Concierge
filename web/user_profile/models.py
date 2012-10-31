from collections import Counter

from django.contrib.auth.models import User
from django.db import models
from managers import UserProfileManager

from recommendation_item.models import Restaurant

# indicates a users initial preferences
class Favorite(models.Model):
  restaurant = models.ForeignKey(Restaurant)

class UserProfile(models.Model):
  access_token = models.CharField(max_length=260, null=True, blank=True)
  singly_id = models.CharField(max_length=260, null=True, blank=True)
  profiles = models.TextField(null=True, blank=True)
  favorites = models.ManyToManyField(Favorite, null=True, blank=True)
  user = models.ForeignKey(User, related_name='profile')

  objects = UserProfileManager()

  class Meta:
    db_table = 'user_profile'

  def get_avg_price (self):
    return sum([f.restaurant.price for f in
               self.favorites.all()])/len(self.favorites.all())

  # returns a dictionary with cuisine and the frequency from the list of user's
  # favorites
  def get_fav_cuisines (self):
    cuisines = []
    for f in self.favorites.all():
      f_cuisines = f.restaurant.cuisines
      [cuisines.append(cuisine) for cuisine in f_cuisines]
    return Counter(cuisines)





