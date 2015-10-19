import json

import django
from django import forms
from django.utils.html import escapejs
from django.shortcuts import resolve_url
from django.contrib.staticfiles.templatetags.staticfiles import static


class AddAnotherMixin(object):
    """Mixin for :class:`Widgets <django.forms.widgets.Widget>` classes that
    adds the *add another* button and the JavaScript required for the popup handling.
    """
    class Media:
        js = ['django_addanother/django_addanother.js']

    #: The URL, pattern name or view name to open in the popup. This may be
    #: None iff :meth:`get_add_another_url` is overwritten.
    add_another_url = None

    def __init__(self, *args, **kwargs):
        if 'add_another_url' in kwargs:
            self.add_another_url = kwargs.pop('add_another_url')
        super(AddAnotherMixin, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, choices=()):
        """Render the parent widget plus the *add another* button.

        This uses ``super().render(...)`` and :meth:`get_add_another_html`.
        """
        base_html = super(AddAnotherMixin, self).render(name, value, attrs, choices)
        return base_html + self.get_add_another_html()

    def get_add_another_html(self):
        """Return the HTML that describes the *add another* button.

        This consists of the JavaScript returned by :meth:`get_popup_opts_js`
        and an ``<a onclick="dj_aa_popup(this)">`` element.
        """
        if django.VERSION < (1, 9):
            add_icon_path = static("admin/img/icon_addlink.gif")
        else:
            add_icon_path = static("admin/img/icon-addlink.svg")
        button_html = '<a href="#" onclick="dj_aa_popup(this); return false"><img src="%s"></a>' % add_icon_path
        return self.get_popup_opts_js() + button_html

    def get_popup_opts_js(self):
        return "<script>var popup_opts = %s</script>" % json.dumps(self.get_popup_opts())

    def get_add_another_url(self):
        """Return the URL of the popup window. This defaults to the :attr:`add_another_url`
        attribute, which is passed to :func:`django.shortcuts.resolve_url`.
        """
        if self.add_another_url is None:
            raise TypeError("Missing 'add_another_url' argument or class attribute")
        return resolve_url(self.add_another_url)

    def get_popup_url(self):
        return self.get_add_another_url() + "?_popup=1&target_elem=" + escapejs(self.attrs['id'])

    def get_popup_size(self):
        """Return the size of the popup window as a ``(width, height)`` tuple.

        Defaults to ``(500, 300)``.
        """
        return (500, 300)

    def get_popup_opts(self):
        w, h = self.get_popup_size()
        url = self.get_popup_url()
        return {
            'width': w,
            'height': h,
            'url': url,
          }


class SelectAddAnother(AddAnotherMixin, forms.Select):
    pass


class SelectMultipleAddAnother(AddAnotherMixin, forms.SelectMultiple):
    pass
