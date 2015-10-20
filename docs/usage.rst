.. _usage:

How to Use
==========

1. Add the *add another* button
-------------------------------
Replace the widget of the form field you want to show the *add another* button next to with the widgets provided by django-addanother:

+----------------------------------------------+--------------------------------------------------------------+
| Stock widget                                 | django-addanother widget                                     |
+==============================================+==============================================================+
| :class:`~django.forms.Select`                | :class:`~django_addanother.widgets.SelectAddAnother`         |
| (:class:`~django.db.models.ForeignKey`)      |                                                              |
+----------------------------------------------+--------------------------------------------------------------+
| :class:`~django.forms.SelectMultiple`        | :class:`~django_addanother.widgets.SelectMultipleAddAnother` |
| (:class:`~django.db.models.ManyToManyField`) |                                                              |
+----------------------------------------------+--------------------------------------------------------------+


For example, let's say we want to add *add another* buttons to a model form::

  from django_addanother.widgets import SelectAddAnother, SelectMultipleAddAnother
  
  class FooForm(forms.ModelForm):
      class Meta:
          ...
          widgets = {
              'sender': SelectAddAnother(add_another_url='person_create'),
              'recipients': SelectMultipleAddAnother(add_another_url='person_create'),
          }

This will add an *add another* button next to the ``sender`` and ``recipients`` fields. When clicked, these will open the ``'person_create'`` URL in a popup.  The ``add_another_url`` keyword argument is passed as-is to :func:`django.shortcuts.resolve_url`, so you may pass full URLs, view names etc. as well.

.. important:: Be sure to include form media in your templates::
  
  {{ form }}
  {{ form.media }}


2. Make your view popup-compatible
----------------------------------
.. note:: This assumes you're using Django's generic :class:`~django.views.generic.edit.CreateView`. django-addanother doesn't support function-based views at the point of writing. You'll have to convert any function-based views to Class Based Views first.

Making your ``CreateView`` compatible with django-addanother is as simple as making it inherit the :class:`django_addanother.views.PopupMixin` class::

  from django_addanother.views import PopupMixin

  class FooCreate(PopupMixin, CreateView):
      model = Foo
      ...

This overwrites your view's :meth:`~django.views.generic.edit.FormMixin.form_valid` method to return a special JavaScript response in case a form has been submitted from a popup.

You may want to hide header, footer and navigation elements for the popups. When the create view is opened in a popup, the ``view.is_popup`` template variable is set:

  .. code-block:: django

    {% if view.is_popup %}
      <nav>...</nav>
    {% endif %}


3. Profit
---------
That's it!
