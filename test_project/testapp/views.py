import django
from django.views import generic
from django_addanother.views import PopupMixin, ChangePopupMixin
from .models import Team, Player
from .forms import TeamForm, PlayerForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

class CreateTeam(PopupMixin, generic.CreateView):
    model = Team
    fields = ['name']

class EditTeam(ChangePopupMixin, generic.UpdateView):
    model = Team
    form_class = TeamForm

def main(request):
    # Player = Player()

    form = PlayerForm()

    context = {
        'form': form,
        'jquery' : 'admin/js/jquery.js' if django.VERSION < (1, 9) else 'admin/js/vendor/jquery/jquery.js',
    }    

    return render(request, 'testapp/main.html', context)

# class UpdatePlayer(generic.UpdateView):
#     model = Player
#     form_class = PlayerForm
#     template_name = 'main.html'
#     success_url = reverse_lazy('main')

#     def get_context_data(self, *args, **kwargs):
#         context = super(UpdatePlayer, self).get_context_data(*args, **kwargs)
#         if django.VERSION < (1, 9):
#             context['jquery'] = 'admin/js/jquery.js'
#         else:
#             context['jquery'] = 'admin/js/vendor/jquery/jquery.js'
#         return context

#     def get_object(self):
#         try:
#             return self.model.objects.first()
#         except self.model.DoesNotExist:
#             return self.model.objects.create(username='test')

