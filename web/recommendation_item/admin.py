from django.contrib import admin
from models import Restaurant, RecommendationItem, RecommendationList, Address

admin.site.register(Restaurant)
admin.site.register(RecommendationList)
admin.site.register(RecommendationItem)
admin.site.register(Address)
