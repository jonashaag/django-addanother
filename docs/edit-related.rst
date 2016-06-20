.. _edit-related:

*Edit related* buttons
======================

Similarly to *add another* buttons (see :ref:`usage`), to add *edit related* buttons to your widget, proceed with the following steps:

1. Wrap your widget with the :class:`AddAnotherEditSelectedWidgetWrapper` class, and provide an edit URL in addition to the add URL.
2. Make your edit view popup-compatible by having it inherit the :class:`django_addanother.views.AddPopupMixin` class.

The edit URL must contain the ``__fk__`` string as a placeholder for the actual object's primary key.  Example::

  # forms.py
  from django.core.urlresolvers import reverse_lazy
  from django_addanother.widgets import AddAnotherEditSelectedWidgetWrapper
  
  class FooForm(forms.ModelForm):
      class Meta:
          ...
          widgets = {
              'sender': AddAnotherEditSelectedWidgetWrapper(
                  forms.Select,
                  reverse_lazy('person_create'),
                  reverse_lazy('person_update', args=['__fk__']),
              )
          }


  # views.py
  from django_addanother.views import ChangePopupMixin

  class PersonUpdate(ChangePopupMixin, UpdateView):
      model = Foo
      ...

If you need the *edit related* button only, but not the *add another*, wrap your widget with the :class:`EditSelectedWidgetWrapper` class and remove the add URL.
