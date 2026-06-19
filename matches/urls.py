from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.match_list,
        name='match_list'
    ),

    path(
        '<int:pk>/',
        views.match_detail,
        name='match_detail'
    ),

    path(
    'team/<int:pk>/',
    views.team_detail,
    name='team_detail'
),

path(
    'team/<int:pk>/',
    views.team_detail,
    name='team_detail'
),

path(
    'analytics/',
    views.analytics,
    name='analytics'
),

path(
    'upcoming/',
    views.upcoming_matches,
    name='upcoming_matches'
),

]