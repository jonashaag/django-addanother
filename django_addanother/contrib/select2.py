import textwrap

import django_select2.forms  # NOQA
import django_addanother.widgets  # NOQA


def _gen_classes(globals_, locals_):
    wrapper_classes = [
        'AddAnotherWidgetWrapper',
        'EditSelectedWidgetWrapper',
        'AddAnotherEditSelectedWidgetWrapper',
    ]
    select2_widgets = [
        'Select2Widget',
        'HeavySelect2Widget',
        'Select2MultipleWidget',
        'HeavySelect2MultipleWidget',
        'HeavySelect2TagWidget',
        'ModelSelect2Widget',
        'ModelSelect2MultipleWidget',
        'ModelSelect2TagWidget',
    ]
    cls_template = textwrap.dedent('''
    class {new_widget_cls}({widget_cls}):
        """:class:`~{widget_cls}` wrapped to remove empty option duplication."""

        def optgroups(self, name, value, attrs=None):
            optgroups = super({new_widget_cls}, self).optgroups(
                name, value, attrs=attrs)
            if not self.is_required and not self.allow_multiple_selected:
                # In this case select2 widget adds one more option.
                # We can just drop it now
                optgroups = optgroups[1:]
            return optgroups

    class {new_cls_name}({wrapper_cls}):
        """:class:`~{widget_cls}` wrapped with :class:`~{wrapper_cls}`."""
        def __init__(self, *args, **kwargs):
            super({new_cls_name}, self).__init__({new_widget_cls}, *args, **kwargs)
    ''')

    for wrapper_cls in wrapper_classes:
        for widget_cls in select2_widgets:
            new_cls_name = widget_cls[:-len("Widget")] + wrapper_cls[:-len("WidgetWrapper")]
            code = cls_template.format(
                new_cls_name=new_cls_name,
                widget_cls="django_select2.forms.%s" % widget_cls,
                new_widget_cls="Fixed%s" % widget_cls,
                wrapper_cls="django_addanother.widgets.%s" % wrapper_cls,
            )
            exec(code, globals_, locals_)
            yield new_cls_name


__all__ = list(_gen_classes(globals(), locals()))

