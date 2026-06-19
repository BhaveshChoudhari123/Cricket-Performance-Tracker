from django.shortcuts import render, redirect, get_object_or_404
from .models import Player
from .forms import PlayerForm
from django.db.models import Sum
from matches.models import BattingScore, BowlingScore


def player_list(request):
    players = Player.objects.all()

    return render(
        request,
        'players/player_list.html',
        {'players': players}
    )


def add_player(request):

    if request.method == 'POST':

        form = PlayerForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect(
                'player_list'
            )

    else:

        form = PlayerForm()

    return render(
        request,
        'players/add_player.html',
        {'form': form}
    )

from django.shortcuts import render, redirect, get_object_or_404
from .models import Player
from .forms import PlayerForm


def edit_player(request, player_id):

    player = get_object_or_404(
        Player,
        id=player_id
    )

    if request.method == 'POST':

        form = PlayerForm(
            request.POST,
            request.FILES,
            instance=player
        )

        if form.is_valid():
            form.save()

            return redirect(
                'player_list'
            )

    else:

        form = PlayerForm(
            instance=player
        )

    return render(
        request,
        'players/edit_player.html',
        {
            'form': form,
            'player': player
        }
    )

def delete_player(request, player_id):

    player = get_object_or_404(
        Player,
        id=player_id
    )

    player.delete()

    return redirect(
        'player_list'
    )

def player_profile(request, player_id):

    player = get_object_or_404(
        Player,
        id=player_id
    )

    return render(
        request,
        'players/profile.html',
        {
            'player': player
        }
    )

def player_profile(request, player_id):

    player = Player.objects.get(id=player_id)

    batting = BattingScore.objects.filter(
        player=player
    )

    bowling = BowlingScore.objects.filter(
        player=player
    )

    total_runs = sum(
        score.runs for score in batting
    )

    total_wickets = sum(
        score.wickets for score in bowling
    )

    context = {
        'player': player,
        'batting': batting,
        'bowling': bowling,
        'total_runs': total_runs,
        'total_wickets': total_wickets,
    }

    return render(
        request,
        'players/player_profile.html',
        context
    )