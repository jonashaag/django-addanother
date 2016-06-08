from django_addanother.widgets import AddAnotherWidgetWrapper, RelatedWidgetWrapper

from django.contrib.auth.models import Group, User
from django.core.urlresolvers import reverse_lazy
from django import forms
from .models import Team, Player


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'current_team', 'future_team', 'previous_teams']
        widgets = {
            'current_team': AddAnotherWidgetWrapper(
                forms.Select,
                reverse_lazy('add_team'),
            ),
            'future_team': RelatedWidgetWrapper(
                forms.Select,
                reverse_lazy('add_team'),
                reverse_lazy('edit_team',args=['__fk__']),
            ),
            'previous_teams': AddAnotherWidgetWrapper(
                forms.SelectMultiple,
                reverse_lazy('add_team'),
            )
        }