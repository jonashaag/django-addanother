from django import http
from django.contrib.admin.options import IS_POPUP_VAR
from django.template.defaultfilters import escapejs
from django.utils import six
from django.utils.encoding import force_text


class PopupMixin(object):
    """Mixin for :class:`~django.views.generic.edit.CreateView` classes that
    handles the case of the view being opened in an *add another* popup window.
    """
    def is_popup(self):
        return self.request.GET.get(IS_POPUP_VAR, False)

    def form_valid(self, form):
        if self.is_popup():
            # If this view is only used with addanother, never as a standalone,
            # then the user may not have set a success url, which causes an
            # ImproperlyConfigured error. (We never use the success url for the
            # addanother popup case anyways, since we always directly close the
            # popup window.)
            self.success_url = '/'
        response = super(PopupMixin, self).form_valid(form)
        if self.is_popup():
            return self.respond_script(self.object)
        else:
            return response

    def respond_script(self, created_obj):
        html = self.get_script_response_html(
            escapejs(six.text_type(self._get_created_obj_pk(created_obj))),
            escapejs(self.label_from_instance(created_obj)),
        )
        return http.HttpResponse(html, status=201)

    def get_script_response_html(self, created_obj_pk, created_obj_label):
        template = '<script>opener.dismissAddAnotherPopup(window, "{pk}", "{label}")</script>'
        return template.format(
            pk=created_obj_pk,
            label=created_obj_label
        )

    def _get_created_obj_pk(self, created_obj):
        pk_name = created_obj._meta.pk.attname
        return created_obj.serializable_value(pk_name)

    def label_from_instance(self, related_instance):
        """Return the label to show in the "main form" for the
        newly created object.

        Overwrite this to customize the label that is being shown.
        """
        return force_text(related_instance)
