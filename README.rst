django-addanother
~~~~~~~~~~~~~~~~~

This app provides a widget wrapper and utilities to add an "Add another"
feature for select inputs just like in django-admin.

This has been extracted from django-autocomplete-light v2, after noticing that
other apps copied the same code, to ease community maintainance.

Install
=======

Install the latest release from PiPy with ``pip install django-addanother``, or
the development version from git with ``pip install -e
https://github.com/yourlabs/django-addanother.git``.

Demo
====

To run the demo, clone the repository and change to the ``test_project``
directory, run ``./manage.py migrate`` and ``./manage.runserver`` then go to
``http://localhost:8000``.

Usage
=====

Make a CreateView that is able to respond with the ``dismissAddAnotherPopup()``
javascript call, or use ``addanother.views.CreateView`` for that::


    from addanother.views import CreateView


    class YourAddView(CreateView):
        model = Group
        fields = ['name']

Add a named url for it::

    url(r'^add/$', YourAddView.as_view(), name='your_add_view'),

You can then use the related widget wrapper in a form::

    from addanother.widgets import AddAnotherWidgetWrapper

    from django.core.urlresolvers import reverse_lazy
    from django import forms


    class TestForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['username', 'groups']
            widgets = {
                'groups': AddAnotherWidgetWrapper(
                    forms.SelectMultiple(choices=Group.objects.all()),
                    reverse_lazy('your_add_view'),
                )
            }

In the template, don't forget to include jQuery and ``{{ form.media }}``, ie.::

    <form action="" method="post">
        {{ form.as_p }}
        {% csrf_token %}
        <input type="submit" value="Submit" />
    </form>

    <script type="text/javascript" src="{% static 'admin/js/vendor/jquery/jquery.js' %}"></script>
    {{ form.media }}
