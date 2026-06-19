from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from .models import Match
from .models import Team
import json

from django.shortcuts import render, get_object_or_404
from .models import Match

def match_list(request):

    matches = Match.objects.all()

    return render(
        request,
        'matches/match_list.html',
        {
            'matches': matches
        }
    )


def add_match(request):

    if request.method == 'POST':

        form = MatchForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'match_list'
            )

    else:

        form = MatchForm()

    return render(
        request,
        'matches/add_match.html',
        {'form': form}
    )

from .models import (
    Match,
    Innings,
    BattingScore,
    BowlingScore,
    Commentary,
    PointsTable,
    Team
)

from players.models import Player


def match_detail(request, pk):

     match = Match.objects.get(id=pk)

     innings_list = Innings.objects.filter(
         match=match
     )

     batting_scores = BattingScore.objects.all()

     bowling_scores = BowlingScore.objects.all()

     commentary = Commentary.objects.filter(
         match=match
     ).order_by('-created_at')

     target = None
     runs_needed = None

     if innings_list.count() >= 2:

         first = innings_list[0]
         second = innings_list[1]

         target = first.runs + 1

         runs_needed = target - second.runs

     points_table = PointsTable.objects.filter(
         tournament=match.tournament
     ).order_by(
         '-points',
         '-net_run_rate'
     )

     orange_cap = (
         BattingScore.objects
         .values('player__name')
         .annotate(
             total_runs=Sum('runs')
         )
         .order_by('-total_runs')[:10]
     )

     purple_cap = (
         BowlingScore.objects
         .values('player__name')
         .annotate(
             total_wickets=Sum('wickets')
         )
         .order_by('-total_wickets')[:10]
     )

     context = {

         'match': match,

         'innings_list': innings_list,

         'batting_scores': batting_scores,

         'bowling_scores': bowling_scores,

         'commentary': commentary,

         'target': target,

         'runs_needed': runs_needed,

         'points_table': points_table,

         'orange_cap': orange_cap,

         'purple_cap': purple_cap,

     }

     return render(
         request,
         'matches/match_detail.html',
         context
     )

def team_detail(request, pk):

    team = Team.objects.get(id=pk)

    players = Player.objects.filter(
        team=team
    )

    matches_played = (
        team.team1_matches.count() +
        team.team2_matches.count()
    )

    wins = team.won_matches.count()

    losses = matches_played - wins

    if matches_played > 0:
        win_percentage = round(
            (wins / matches_played) * 100,
            2
        )
    else:
        win_percentage = 0

    context = {
        'team': team,
        'players': players,
        'matches_played': matches_played,
        'wins': wins,
        'losses': losses,
        'win_percentage': win_percentage,
    }

    return render(
        request,
        'matches/team_detail.html',
        context
    )

def analytics(request):

    top_run_scorers = (
        BattingScore.objects
        .values('player__name')
        .annotate(
            total_runs=Sum('runs')
        )
        .order_by('-total_runs')[:5]
    )

    top_wicket_takers = (
        BowlingScore.objects
        .values('player__name')
        .annotate(
            total_wickets=Sum('wickets')
        )
        .order_by('-total_wickets')[:5]
    )

    run_labels = [
        player['player__name']
        for player in top_run_scorers
    ]

    run_data = [
        player['total_runs']
        for player in top_run_scorers
    ]

    wicket_labels = [
        player['player__name']
        for player in top_wicket_takers
    ]

    wicket_data = [
        player['total_wickets']
        for player in top_wicket_takers
    ]

    context = {

        'top_run_scorers': top_run_scorers,
        'top_wicket_takers': top_wicket_takers,

        'run_labels': json.dumps(run_labels),
        'run_data': json.dumps(run_data),
        'wicket_labels': json.dumps(wicket_labels),
        'wicket_data': json.dumps(wicket_data),
    }

    return render(
        request,
        'matches/analytics.html',
        context
    )

def upcoming_matches(request):

    matches = Match.objects.filter(
        status='Upcoming'
    ).order_by('match_date')

    return render(
        request,
        'matches/upcoming_matches.html',
        {
            'matches': matches
        }
    )