from django import http
from django.contrib.admin.options import IS_POPUP_VAR
from django.template.defaultfilters import escapejs
from django.utils import six
from django.views import generic


class CreateView(generic.CreateView):
    def is_popup(self):
        return self.request.GET.get(IS_POPUP_VAR, False)

    def respond_script(self, obj=None):
        if obj is None:
            obj = self.object

        value = obj.serializable_value(obj._meta.pk.attname)

        html = ['<!DOCTYPE html>', '<html><body>']
        html.append('<script type="text/javascript">')
        html.append(
            'opener.dismissAddAnotherPopup( window, "%s", "%s" );' % (
                escapejs(six.text_type(value)),
                escapejs(six.text_type(obj))
            )
        )
        html.append('</script></body></html>')

        html = ''.join(html)

        return http.HttpResponse(html, status=201)

    def form_valid(self, form):
        """ If request.GET._popup, return some javascript. """
        if self.is_popup():
            self.success_url = '/'  # avoid ImproperlyConfigured

        response = super(CreateView, self).form_valid(form)

        if not self.is_popup():
            return response

        return self.respond_script()
