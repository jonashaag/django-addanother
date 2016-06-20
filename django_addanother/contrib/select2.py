import textwrap

from django.utils import six

import django_select2.forms
import django_addanother.widgets


def _gen_classes(globals_, locals_):
    wrapper_classes = [
        'AddAnother',
        'EditSelected',
        'AddAnotherEditSelected',
    ]
    select2_widgets = [
        'Select2',
        'HeavySelect2',
        'Select2Multiple',
        'HeavySelect2Multiple',
        'HeavySelect2Tag',
        'ModelSelect2',
        'ModelSelect2Multiple',
        'ModelSelect2Tag',
    ]
    cls_template = textwrap.dedent("""
    class {cls_name}(django_addanother.widgets.{wrapper_cls}WidgetWrapper):
        def __init__(self, *args, **kwargs):
            super({cls_name}, self).__init__(
                django_select2.forms.{widget_cls}Widget,
                *args, **kwargs
            )
    """)

    for wrapper_cls in wrapper_classes:
        for widget_cls in select2_widgets:
            cls_name = wrapper_cls + widget_cls
            code = cls_template.format(
                cls_name=cls_name,
                widget_cls=widget_cls,
                wrapper_cls=wrapper_cls
            )
            six.exec_(code, globals_, locals_)
            yield cls_name


__all__ = list(_gen_classes(globals(), locals()))
