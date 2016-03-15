Select2 Integration
===================
django-addanother provides optional lightweight integration with django-select2_.

Usage example:

.. code-block:: python

  from django_addanother.contrib.select2 import Select2AddAnother

  class FooForm(forms.ModelForm):
      class Meta:
          ...
          widgets = {
              'sender': Select2AddAnother(reverse_lazy('person_create')),
          }


See :ref:`select2ref` for a list of provided widgets.

.. _django-select2: http://django-select2.readthedocs.org/
