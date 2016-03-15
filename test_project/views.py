import django
from django.contrib.auth.models import Group, User
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from django_addanother.views import PopupMixin

from forms import TestForm


class CreateGroup(PopupMixin, generic.CreateView):
    model = Group
    fields = ['name']


class MainView(generic.UpdateView):
    model = User
    form_class = TestForm
    template_name = 'form.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, *args, **kwargs):
        context = super(MainView, self).get_context_data(*args, **kwargs)
        if django.VERSION < (1, 9):
            context['jquery'] = 'admin/js/jquery.js'
        else:
            context['jquery'] = 'admin/js/vendor/jquery/jquery.js'
        return context

    def get_object(self):
        try:
            return User.objects.first()
        except User.DoesNotExist:
            return User.objects.create(username='test')
