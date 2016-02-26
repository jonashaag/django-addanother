from addanother.widgets import AddAnotherWidgetWrapper

from django.contrib.auth.models import Group, User
from django.core.urlresolvers import reverse_lazy
from django import forms


class TestForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'groups']
        widgets = {
            'groups': AddAnotherWidgetWrapper(
                forms.SelectMultiple(choices=Group.objects.all()),
                reverse_lazy('add'),
            )
        }
