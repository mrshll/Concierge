from django.con.urls import patterns, url

urlpatterns = patterns('survey.views',
        url(r'favorites/', 'favorites'),

)
