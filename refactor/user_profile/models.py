from django.db import models
from django.contrib.auth.models import User
from managers import UserProfileManager

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name='profile')
    access_token = models.CharField(max_length=260, null=True, blank=True)
    singly_id = models.CharField(max_length=260, null=True, blank=True)
    profiles = models.TextField(null=True, blank=True)

    fb_data = models.CharField(max_length=10000)
    objects = UserProfileManager()

    class Meta:
      db_table = 'user_profile'

    # static Facebook vector, fb_data, holds:
    """
    Where you live
    Schools
    Birthday/Age
    Gender
    Sexual orientation
    Languages
    Likes
    (Count for each like category)
    Map tags
    Friend Count
    """
