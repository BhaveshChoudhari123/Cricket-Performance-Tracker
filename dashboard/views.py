from django.shortcuts import render
import requests

from players.models import Player
from matches.models import Match


def dashboard(request):

    total_players = Player.objects.count()
    total_matches = Match.objects.count()

    live_matches = []

    try:

        api_key = "06ba6c7f-c6f4-41c6-b0a7-d21a9abfe192"

        url = (
            f"https://api.cricapi.com/v1/currentMatches"
            f"?apikey={api_key}&offset=0"
        )

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=30
        )

        print("STATUS:", response.status_code)
        print("TEXT:", response.text)

        data = response.json()

        print(data)

        if data.get("status") == "success":
            live_matches = data.get("data", [])

    except Exception as e:
        print("Dashboard Error:", e)

    context = {
        "total_players": total_players,
        "total_matches": total_matches,
        "live_matches": live_matches[:5],
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )