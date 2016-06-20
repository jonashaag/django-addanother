import django
from django.views import generic
from django.shortcuts import render

from django_addanother.views import CreatePopupMixin, UpdatePopupMixin

from .models import Team
from .forms import PlayerForm


class CreateTeam(CreatePopupMixin, generic.CreateView):
    model = Team
    fields = ['name']


class EditTeam(UpdatePopupMixin, generic.UpdateView):
    model = Team
    fields = ['name']


def main(request):
    form = PlayerForm()
    context = {
        'form': form,
        'jquery': 'admin/js/jquery.js' if django.VERSION < (1, 9) else 'admin/js/vendor/jquery/jquery.js',
    }
    return render(request, 'testapp/main.html', context)
