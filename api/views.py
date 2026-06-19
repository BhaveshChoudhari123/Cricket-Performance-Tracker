import requests
from django.shortcuts import render


def live_matches(request):

    API_KEY = "06ba6c7f-c6f4-41c6-b0a7-d21a9abfe192"

    url = "https://api.cricapi.com/v1/currentMatches"

    params = {
        "apikey": API_KEY,
        "offset": 0
    }

    response = requests.get(
        url,
        params=params
    )

    data = response.json()

    print(data)

    print("TOTAL MATCHES =", len(data.get("data", [])))

    matches = data.get("data", [])

    print("MATCHES DATA")
    print(matches)

    return render(
        request,
        "api/live_matches.html",
        {
            "matches": matches
        }
    )


def match_detail(request, match_id):

    api_key = "06ba6c7f-c6f4-41c6-b0a7-d21a9abfe192"

    url = (
        f"https://api.cricapi.com/v1/match_scorecard"
        f"?apikey={api_key}"
        f"&id={match_id}"
    )

    match = {}

    batting = []
    bowling = []
    yet_to_bat = []

    prediction = "Prediction Not Available"

    team1_probability = 50
    team2_probability = 50

    try:

        response = requests.get(url)

        data = response.json()

        print(data)

        if data.get("status") == "success":

            match = data.get(
                "data",
                {}
            )

            scorecard = match.get(
                "scorecard",
                []
            )

            all_scorecards = []

            if scorecard:

                print("SCORECARD DATA")
                print(scorecard)

                for innings in scorecard:

                    print("BATTING DATA")
                    print(innings.get("batting", []))

                    all_scorecards.append({

                        "inning": innings.get(
                            "inning",
                            "Unknown Innings"
                        ),

                        "batting": innings.get(
                            "batting",
                            []
                        ),

                        "bowling": innings.get(
                            "bowling",
                            []
                        ),

                    })

            if match.get("score"):

                score = match.get(
                    "score",
                    []
                )

                if len(score) >= 2:

                    first_runs = score[0].get(
                        "r",
                        0
                    )

                    second_runs = score[1].get(
                        "r",
                        0
                    )

                    total_runs = (
                        first_runs +
                        second_runs
                    )

                    if total_runs > 0:

                        team1_probability = round(
                            (
                                first_runs /
                                total_runs
                            ) * 100
                        )

                        team2_probability = round(
                            (
                                second_runs /
                                total_runs
                            ) * 100
                        )

                    teams = match.get(
                        "teams",
                        []
                    )

                    if len(teams) >= 2:

                        if first_runs > second_runs:

                            prediction = (
                                f"{teams[0]} has higher winning chance"
                            )

                        elif second_runs > first_runs:

                            prediction = (
                                f"{teams[1]} has higher winning chance"
                            )

                        else:

                            prediction = (
                                "Match is evenly balanced"
                            )

    except Exception as e:

        print(
            "Match Detail Error:",
            e
        )

    context = {

        "match": match,

        "all_scorecards": all_scorecards,

        "yet_to_bat": yet_to_bat,

        "prediction": prediction,

        "team1_probability": team1_probability,

        "team2_probability": team2_probability,

    }

    return render(
        request,
        "api/match_detail.html",
        context
    )


def points_table(request):

    teams = [

        {
            "name": "Chennai Super Kings",
            "matches": 14,
            "wins": 10,
            "losses": 4,
            "points": 20,
            "nrr": 1.12
        },

        {
            "name": "Mumbai Indians",
            "matches": 14,
            "wins": 9,
            "losses": 5,
            "points": 18,
            "nrr": 0.95
        },

        {
            "name": "Royal Challengers Bengaluru",
            "matches": 14,
            "wins": 8,
            "losses": 6,
            "points": 16,
            "nrr": 0.75
        },

        {
            "name": "Kolkata Knight Riders",
            "matches": 14,
            "wins": 7,
            "losses": 7,
            "points": 14,
            "nrr": 0.42
        },

    ]

    return render(
        request,
        "api/points_table.html",
        {
            "teams": teams
        }
    )


def player_rankings(request):

    top_batsmen = [

        {
            "name": "Virat Kohli",
            "runs": 850
        },

        {
            "name": "Rohit Sharma",
            "runs": 790
        },

        {
            "name": "Shubman Gill",
            "runs": 740
        },

        {
            "name": "KL Rahul",
            "runs": 680
        },

    ]

    top_bowlers = [

        {
            "name": "Jasprit Bumrah",
            "wickets": 27
        },

        {
            "name": "Mohammed Shami",
            "wickets": 24
        },

        {
            "name": "Kuldeep Yadav",
            "wickets": 22
        },

        {
            "name": "Arshdeep Singh",
            "wickets": 20
        },

    ]

    context = {

        "top_batsmen": top_batsmen,

        "top_bowlers": top_bowlers,

    }

    return render(
        request,
        "api/player_rankings.html",
        context
    )

def analytics(request):

    return render(
        request,
        'api/analytics.html'
    )

def team_rankings(request):

    teams = [

        {
            "name": "India",
            "rating": 125,
            "points": 4500
        },

        {
            "name": "Australia",
            "rating": 121,
            "points": 4300
        },

        {
            "name": "England",
            "rating": 118,
            "points": 4100
        },

        {
            "name": "South Africa",
            "rating": 115,
            "points": 3950
        },

    ]

    return render(
        request,
        'api/team_rankings.html',
        {
            'teams': teams
        }
    )

import requests
from django.http import JsonResponse


def test_scorecard(request):

    api_key = "YOUR_API_KEY"

    match_id = "PUT_ANY_MATCH_ID_HERE"

    url = (
        f"https://api.cricapi.com/v1/match_info"
        f"?apikey={api_key}"
        f"&id={match_id}"
    )

    response = requests.get(url)

    return JsonResponse(response.json())

def upcoming_matches(request):

    api_key = "YOUR_API_KEY"

    url = (
        f"https://api.cricapi.com/v1/matches"
        f"?apikey={api_key}"
    )

    matches = []

    try:

        response = requests.get(url)

        data = response.json()

        if data.get("status") == "success":

            all_matches = data.get("data", [])

            for match in all_matches:

                if not match.get("matchStarted", False):

                    matches.append(match)

    except Exception as e:

        print("Upcoming Match Error:", e)

    return render(
        request,
        "api/upcoming_matches.html",
        {
            "matches": matches
        }
    )

def completed_matches(request):

    api_key = "06ba6c7f-c6f4-41c6-b0a7-d21a9abfe192"

    url = (
        f"https://api.cricapi.com/v1/currentMatches"
        f"?apikey={api_key}"
        f"&offset=0"
    )

    matches = []

    try:

        response = requests.get(url)

        data = response.json()

        if data.get("status") == "success":

            all_matches = data.get(
                "data",
                []
            )

            for match in all_matches:

                if match.get(
                    "matchEnded",
                    False
                ):

                    matches.append(
                        match
                    )

    except Exception as e:

        print(
            "Completed Match Error:",
            e
        )

    return render(
        request,
        "api/completed_matches.html",
        {
            "matches": matches
        }
    )