from django import forms
from .models import Match

class MatchForm(forms.ModelForm):

    class Meta:
        model = Match

        fields = [
            'tournament',
            'team1',
            'team2',
            'venue',
            'match_date',
            'status',
            'winner'
        ]

        widgets = {
            'match_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}
            )
        }