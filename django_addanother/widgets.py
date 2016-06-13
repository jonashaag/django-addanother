import django
from django import forms
from django.contrib.admin.views.main import IS_POPUP_VAR
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


if django.VERSION < (1, 9):
    DEFAULT_ADD_ICON = 'admin/img/icon_addlink.gif'
    DEFAULT_EDIT_ICON = 'admin/img/icon_changelink.gif'
else:
    DEFAULT_ADD_ICON = 'admin/img/icon-addlink.svg'
    DEFAULT_EDIT_ICON = 'admin/img/icon-changelink.svg'


# Most of the wrapper code that follows is copied/inspired by Django's
# RelatedFieldWidgetWrapper.

class WidgetWrapperMixin(object):
    @property
    def is_hidden(self):
        return self.widget.is_hidden

    @property
    def media(self):
        return self.widget.media

    def build_attrs(self, extra_attrs=None, **kwargs):
        "Helper function for building an attribute dictionary."
        self.attrs = self.widget.build_attrs(extra_attrs=None, **kwargs)
        return self.attrs

    def value_from_datadict(self, data, files, name):
        return self.widget.value_from_datadict(data, files, name)

    def id_for_label(self, id_):
        return self.widget.id_for_label(id_)


class RelatedWidgetWrapper(WidgetWrapperMixin, forms.Widget):
    #: The template that is used to render the *add another* button.
    #: Overwrite this to customize the rendering.
    template = 'django_addanother/related_widget_wrapper.html'

    class Media:
        css = {
            'all': ('django_addanother/addanother.css',)
        }
        js = (
            'django_addanother/django_jquery.js',
            'admin/js/admin/RelatedObjectLookups.js',
        )
        if django.VERSION < (1, 9):
            # This is part of "RelatedObjectLookups.js" in Django 1.9
            js += ('admin/js/related-widget-wrapper.js',)

    def __init__(self, widget, add_related_url,
                 edit_related_url, add_icon=None, edit_icon=None):
        if isinstance(widget, type):
            widget = widget()
        if add_icon is None:
            add_icon = DEFAULT_ADD_ICON
        if edit_icon is None:
            edit_icon = DEFAULT_EDIT_ICON
        self.widget = widget
        self.attrs = widget.attrs
        self.add_related_url = add_related_url
        self.add_icon = add_icon
        self.edit_related_url = edit_related_url
        self.edit_icon = edit_icon

    def render(self, name, value, *args, **kwargs):
        self.widget.choices = self.choices

        url_params = "%s=%s" % (IS_POPUP_VAR, 1)
        context = {
            'widget': self.widget.render(name, value, *args, **kwargs),
            'name': name,
            'url_params': url_params,
            'add_related_url': self.add_related_url,
            'add_icon': self.add_icon,
            'edit_related_url': self.edit_related_url,
            'edit_icon': self.edit_icon,
        }
        return mark_safe(render_to_string(self.template, context))


class AddAnotherWidgetWrapper(RelatedWidgetWrapper):
    def __init__(self, widget, add_related_url, add_icon=None):
        super(AddAnotherWidgetWrapper, self).__init__(
            widget, add_related_url, None, add_icon, None
        )


class EditSelectedWidgetWrapper(RelatedWidgetWrapper):
    def __init__(self, widget, edit_related_url, edit_icon=None):
        super(EditSelectedWidgetWrapper, self).__init__(
            widget, None, edit_related_url, None, edit_icon
        )
