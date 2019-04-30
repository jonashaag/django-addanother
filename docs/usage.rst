.. _usage:

How to Use
==========

1. Add the add-another button
-------------------------------
Wrap :class:`django_addanother.widgets.AddAnotherWidgetWrapper` around your widget to show the add-another button next to it.

For example, let's say we want to add add-another buttons to a model form::

  from django.urls import reverse_lazy
  from django_addanother.widgets import AddAnotherWidgetWrapper
  
  class FooForm(forms.ModelForm):
      class Meta:
          ...
          widgets = {
              'sender': AddAnotherWidgetWrapper(
                  forms.Select,
                  reverse_lazy('person_create'),
              ),
              'recipients': AddAnotherWidgetWrapper(
                  forms.SelectMultiple,
                  reverse_lazy('person_create'),
              )
          }

This will add an add-another button next to the ``sender`` and ``recipients`` fields. When clicked, these will open the ``'person_create'`` URL in a popup.

.. important::
  Be sure to include form media and jQuery in your templates:
  
  .. code-block:: django

    {{ form }}
    <script src="{% static 'admin/js/vendor/jquery/jquery.js' %}"></script>
    {{ form.media }}


2. Make your view popup-compatible
----------------------------------
.. note:: This assumes you're using Django's generic :class:`~django.views.generic.edit.CreateView`. django-addanother doesn't support function-based views at the point of writing. You'll have to convert any function-based views to Class Based Views first.

Making your ``CreateView`` compatible with django-addanother is as simple as making it inherit the :class:`django_addanother.views.CreatePopupMixin` class::

  from django_addanother.views import CreatePopupMixin

  class PersonCreate(CreatePopupMixin, CreateView):
      model = Foo
      ...

This overwrites your view's :meth:`~django.views.generic.edit.FormMixin.form_valid` method to return a special JavaScript response in case a form has been submitted from a popup.

You may want to hide header, footer and navigation elements for the popups. When the create view is opened in a popup, the ``view.is_popup`` template variable is set:

  .. code-block:: django

    {% if not view.is_popup %}
      <nav>...</nav>
    {% endif %}


3. Profit
---------
That's it!

See :ref:`edit-related` on how to add edit buttons too.
