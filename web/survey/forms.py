from django import forms
from recommendation_item.models import Restaurant

class UserSurvey(forms.Form):
  favorites = forms.ModelMultipleChoiceField(queryset=Restaurant.objects.all())
