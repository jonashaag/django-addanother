import django
from django.views import generic
from django.shortcuts import render
from django_addanother.views import AddPopupMixin, ChangePopupMixin
from .models import Team
from .forms import TeamForm, PlayerForm

class CreateTeam(AddPopupMixin, generic.CreateView):
    model = Team
    fields = ['name']

class EditTeam(ChangePopupMixin, generic.UpdateView):
    model = Team
    form_class = TeamForm

def main(request):

    form = PlayerForm()

    context = {
        'form': form,
        'jquery': 'admin/js/jquery.js' if django.VERSION < (1, 9) else 'admin/js/vendor/jquery/jquery.js',
    }

    return render(request, 'testapp/main.html', context)
