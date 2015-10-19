from django.http import HttpResponse, Http404
from django.utils.encoding import force_text
import json


class PopupMixin(object):
    """Mixin for :class:`~django.views.generic.edit.CreateView` classes that
    handles the case of the view being opened in an *add another* popup window.
    """
    def form_valid(self, form):
        response = super(PopupMixin, self).form_valid(form)
        if self.is_popup():
            return self.form_valid_popup(form)
        else:
            return response

    def is_popup(self):
        return self.request.GET.get('_popup')

    def post(self, *args, **kwargs):
        if self.is_popup() and 'target_elem' not in self.request.GET:
            raise Http404("'target_elem' GET parameter missing")
        return super(PopupMixin, self).post(*args, **kwargs)

    def form_valid_popup(self, form):
        objinfo = self.get_js_obj_info(form.instance)
        return HttpResponse(self.get_js_template() % json.dumps(objinfo))

    def get_js_template(self):
        return """<script>
          opener.dj_aa_addNewlyCreatedObject(%s);
          window.close();
        </script>
        """

    def get_js_obj_info(self, instance):
        return {
          'target_elem': self.request.GET['target_elem'],
          'pk': instance.pk,
          'label': self.label_from_instance(instance),
        }

    def label_from_instance(self, instance):
        return force_text(instance)
