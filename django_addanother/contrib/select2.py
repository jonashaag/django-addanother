from django_select2.forms import (
    Select2Widget,
    HeavySelect2Widget,
    Select2MultipleWidget,
    HeavySelect2MultipleWidget,
    HeavySelect2TagWidget,
    ModelSelect2Widget,
    ModelSelect2MultipleWidget,
    ModelSelect2TagWidget,
)

from ..widgets import AddAnotherWidgetWrapper


class Select2WidgetWrapper(AddAnotherWidgetWrapper):
    def __init__(self, add_related_url, add_icon=None):
        super(Select2WidgetWrapper, self).__init__(
            self.widget_class,
            add_related_url,
            add_icon,
        )


class Select2AddAnother(Select2WidgetWrapper):
    widget_class = Select2Widget


class HeavySelect2AddAnother(Select2WidgetWrapper):
    widget_class = HeavySelect2Widget


class Select2MultipleAddAnother(Select2WidgetWrapper):
    widget_class = Select2MultipleWidget


class HeavySelect2MultipleAddAnother(Select2AddAnother):
    widget_class = HeavySelect2MultipleWidget


class HeavySelect2TagAddAnother(Select2AddAnother):
    widget_class = HeavySelect2TagWidget


class ModelSelect2AddAnother(Select2AddAnother):
    widget_class = ModelSelect2Widget


class ModelSelect2MultipleAddAnother(Select2AddAnother):
    widget_class = ModelSelect2MultipleWidget


class ModelSelect2TagAddAnother(Select2AddAnother):
    widget_class = ModelSelect2TagWidget
