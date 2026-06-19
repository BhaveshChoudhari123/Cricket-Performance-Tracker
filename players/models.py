from django.db import models

class Player(models.Model):

    ROLE_CHOICES = [
        ('Batsman', 'Batsman'),
        ('Bowler', 'Bowler'),
        ('All Rounder', 'All Rounder'),
        ('Wicket Keeper', 'Wicket Keeper'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    batting_style = models.CharField(max_length=50)

    bowling_style = models.CharField(
        max_length=50,
        blank=True
    )

    player_image = models.ImageField(
        upload_to='players/',
        blank=True,
        null=True
    )

    # Statistics

    matches = models.IntegerField(default=0)

    runs = models.IntegerField(default=0)

    wickets = models.IntegerField(default=0)

    average = models.FloatField(default=0)

    strike_rate = models.FloatField(default=0)

    hundreds = models.IntegerField(default=0)

    fifties = models.IntegerField(default=0)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name