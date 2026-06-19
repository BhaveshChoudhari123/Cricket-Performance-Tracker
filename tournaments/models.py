from django.db import models


class Tournament(models.Model):

    name = models.CharField(
        max_length=200
    )

    season = models.CharField(
        max_length=50
    )

    start_date = models.DateField()

    end_date = models.DateField()

    def __str__(self):

        return self.name