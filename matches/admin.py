from django.contrib import admin

from .models import (
    Team,
    Tournament,
    Match,
    Innings,
    BattingScore,
    BowlingScore,
    Commentary,
    PointsTable
)

admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(Match)
admin.site.register(Innings)
admin.site.register(BattingScore)
admin.site.register(BowlingScore)
admin.site.register(Commentary)
admin.site.register(PointsTable)