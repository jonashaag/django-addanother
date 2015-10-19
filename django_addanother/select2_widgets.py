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

from .widgets import AddAnotherMixin


class Select2AddAnother(AddAnotherMixin, Select2Widget):
    pass

class HeavySelect2AddAnother(AddAnotherMixin, HeavySelect2Widget):
    pass

class Select2MultipleAddAnother(AddAnotherMixin, Select2MultipleWidget):
    pass

class HeavySelect2MultipleAddAnother(AddAnotherMixin, HeavySelect2MultipleWidget):
    pass

class HeavySelect2TagAddAnother(AddAnotherMixin, HeavySelect2TagWidget):
    pass

class ModelSelect2AddAnother(AddAnotherMixin, ModelSelect2Widget):
    pass

class ModelSelect2MultipleAddAnother(AddAnotherMixin, ModelSelect2MultipleWidget):
    pass

class ModelSelect2TagAddAnother(AddAnotherMixin, ModelSelect2TagWidget):
    pass
