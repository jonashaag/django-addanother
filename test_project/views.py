from django import VERSION
from django.contrib.auth.models import Group, User
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from addanother.views import CreateView

from forms import TestForm


class AddView(CreateView):
    model = Group
    fields = ['name']


class FormView(generic.UpdateView):
    model = User
    form_class = TestForm
    template_name = 'form.html'
    success_url = reverse_lazy('form')

    def get_context_data(self, *args, **kwargs):
        context = super(FormView, self).get_context_data(*args, **kwargs)

        if VERSION < (1, 9):
            context['jquery'] = 'admin/js/jquery.js'
        else:
            context['jquery'] = 'admin/js/vendor/jquery/jquery.js'

        return context

    def get_object(self):
        try:
            return User.objects.first()
        except User.DoesNotExist:
            return User.objects.create(username='test')
