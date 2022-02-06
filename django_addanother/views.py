import json
import sys

import django
from django.contrib.admin.options import IS_POPUP_VAR
from django.template.response import SimpleTemplateResponse
try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_str as force_text


PY2 = sys.version_info[0] == 2


def text_type(value):
    return unicode(value) if PY2 else str(value)


class BasePopupMixin(object):
    """Base mixin for generic views classes that handles the case of the view
    being opened in a popup window.

    Don't call this directly, use some of the subclasses instead.

    .. versionadded:: 2.0.0
       Factored from the original ``PopupMixin`` class.
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
        response = super(BasePopupMixin, self).form_valid(form)
        if self.is_popup():
            return self.respond_script(self.object)
        else:
            return response

    def respond_script(self, created_obj):
        ctx = {
            'action': self.POPUP_ACTION,
            'value': text_type(self._get_created_obj_pk(created_obj)),
            'obj': text_type(self.label_from_instance(created_obj)),
            'new_value': text_type(self._get_created_obj_pk(created_obj))
        }
        if django.VERSION >= (1, 10):
            ctx = {'popup_response_data': json.dumps(ctx)}
        return SimpleTemplateResponse('admin/popup_response.html', ctx)

    def _get_created_obj_pk(self, created_obj):
        pk_name = created_obj._meta.pk.attname
        return created_obj.serializable_value(pk_name)

    def label_from_instance(self, related_instance):
        """Return the label to show in the "main form" for the
        newly created object.

        Overwrite this to customize the label that is being shown.
        """
        return force_text(related_instance)


class CreatePopupMixin(BasePopupMixin):
    """Mixin for :class:`~django.views.generic.edit.CreateView` classes that
    handles the case of the view being opened in an add-another popup window.

    .. versionchanged:: 2.0.0
       This used to be called ``PopupMixin`` and has been renamed with the
       introduction of edit-related buttons and :class:`UpdatePopupMixin`.
    """

    POPUP_ACTION = 'add'


class UpdatePopupMixin(BasePopupMixin):
    """Mixin for :class:`~django.views.generic.edit.UpdateView` classes that
    handles the case of the view being opened in an edit-related popup window.

    .. versionadded:: 2.0.0
    """

    POPUP_ACTION = 'change'
