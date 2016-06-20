from django import forms
from django.core.urlresolvers import reverse_lazy

from django_addanother.widgets import AddAnotherWidgetWrapper, AddAnotherEditSelectedWidgetWrapper

from .models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'current_team', 'future_team', 'previous_teams']
        widgets = {
            'current_team': AddAnotherWidgetWrapper(
                forms.Select,
                reverse_lazy('add_team'),
            ),
            'future_team': AddAnotherEditSelectedWidgetWrapper(
                forms.Select,
                reverse_lazy('add_team'),
                reverse_lazy('edit_team',args=['__fk__']),
            ),
            'previous_teams': AddAnotherWidgetWrapper(
                forms.SelectMultiple,
                reverse_lazy('add_team'),
            )
        }
