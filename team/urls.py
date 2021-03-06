from django.conf.urls import url
from . import views

app_name = 'team'


urlpatterns = [
    #/team/
    url(r'^$',views.index, name='index' ),

    #/team/712/
    url(r'^(?P<team_id>[0-9]+)/$', views.detail , name='detail'),


    # /team/standings/
    url(r'^standings/', views.standings, name='standings'),

    # /team/statistics
    url(r'^statistics', views.statistics, name='statistics'),

    # /team/coach/
    url(r'^coach', views.coach, name='coach'),

    #team/712/52
    url(r'^(?P<team_id>[0-9]+)/(?P<player_id>[0-9]+)/$', views.stats, name = 'player_detail'),

    # /team/contact/
    url(r'^contact/$', views.contact, name='contact'),

    # /team/contact/
    url(r'^institutional/$', views.insti, name='insti'),


]