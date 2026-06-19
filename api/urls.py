from django.urls import path
from . import views

urlpatterns = [

    path(
        'live/',
        views.live_matches,
        name='live_matches'
    ),

    path(
        "match/<str:match_id>/",
        views.match_detail,
        name="match_detail"
    ),

    path(
        'points-table/',
        views.points_table,
        name='points_table'
    ),

    path(
        'player-rankings/',
        views.player_rankings,
        name='player_rankings'
    ),

    path(
        'analytics/',
        views.analytics,
        name='analytics'
    ),

    path(
        'team-rankings/',
        views.team_rankings,
        name='team_rankings'
    ),

    path(
        'test-scorecard/',
        views.test_scorecard,
        name='test_scorecard'
    ),

    path(
        "upcoming-matches/",
        views.upcoming_matches,
        name="upcoming_matches"
    ),

    path(
        "completed-matches/",
        views.completed_matches,
        name="completed_matches"
    ),

]