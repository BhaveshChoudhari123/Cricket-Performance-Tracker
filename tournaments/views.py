from django.shortcuts import render, redirect

from .models import Tournament
from .forms import TournamentForm


def tournament_list(request):

    tournaments = Tournament.objects.all()

    return render(
        request,
        'tournaments/tournament_list.html',
        {
            'tournaments': tournaments
        }
    )


def add_tournament(request):

    if request.method == "POST":

        form = TournamentForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'tournament_list'
            )

    else:

        form = TournamentForm()

    return render(
        request,
        'tournaments/add_tournament.html',
        {
            'form': form
        }
    )