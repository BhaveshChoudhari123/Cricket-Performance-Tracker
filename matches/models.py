from django.db import models
from players.models import Player


class Team(models.Model):

    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    logo = models.ImageField(
        upload_to='teams/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Tournament(models.Model):

    name = models.CharField(max_length=200)

    season = models.CharField(max_length=20)

    logo = models.ImageField(
        upload_to='tournaments/',
        blank=True,
        null=True
    )

    start_date = models.DateField()

    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.season}"


class Match(models.Model):

    MATCH_STATUS = [
        ('Upcoming', 'Upcoming'),
        ('Live', 'Live'),
        ('Completed', 'Completed'),
    ]

    team1 = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='team1_matches'
    )

    team2 = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='team2_matches'
    )

    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE,
        related_name='matches',
        null=True,
        blank=True
    )

    venue = models.CharField(max_length=200)

    match_date = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=MATCH_STATUS,
        default='Upcoming'
    )

    winner = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='won_matches'
    )

    def __str__(self):
        return f"{self.team1} vs {self.team2}"


# ==========================
# INNINGS MODEL
# ==========================

class Innings(models.Model):

    match = models.ForeignKey(
        Match,
        on_delete=models.CASCADE
    )

    batting_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )

    innings_number = models.IntegerField()

    runs = models.IntegerField(default=0)

    wickets = models.IntegerField(default=0)

    overs = models.FloatField(default=0)

    def __str__(self):
        return f"{self.batting_team} - {self.runs}/{self.wickets}"


# ==========================
# BATTING SCORE MODEL
# ==========================

class BattingScore(models.Model):

    innings = models.ForeignKey(
        Innings,
        on_delete=models.CASCADE
    )

    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE
    )

    runs = models.IntegerField(default=0)

    balls = models.IntegerField(default=0)

    fours = models.IntegerField(default=0)

    sixes = models.IntegerField(default=0)

    strike_rate = models.FloatField(default=0)

    def __str__(self):
        return self.player.name


# ==========================
# BOWLING SCORE MODEL
# ==========================

class BowlingScore(models.Model):

    innings = models.ForeignKey(
        Innings,
        on_delete=models.CASCADE
    )

    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE
    )

    overs = models.FloatField(default=0)

    maidens = models.IntegerField(default=0)

    runs = models.IntegerField(default=0)

    wickets = models.IntegerField(default=0)

    economy = models.FloatField(default=0)

    def __str__(self):
        return self.player.name
    
    
class Commentary(models.Model):

    match = models.ForeignKey(
        Match,
        on_delete=models.CASCADE
    )

    over = models.CharField(
        max_length=10
    )

    event = models.CharField(
        max_length=50
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.over} - {self.event}"
    
class PointsTable(models.Model):

    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )

    matches_played = models.IntegerField(
        default=0
    )

    wins = models.IntegerField(
        default=0
    )

    losses = models.IntegerField(
        default=0
    )

    points = models.IntegerField(
        default=0
    )

    net_run_rate = models.FloatField(
        default=0.0
    )

    def __str__(self):
        return f"{self.team} - {self.points}"