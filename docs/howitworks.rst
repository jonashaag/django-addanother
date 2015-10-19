How it Works
============
django-addanother works twofold: Firstly, it adds an *add another* button next to your form fields. When the *add* button is clicked, the main form is disabled by putting an overlay over the whole main site, and a special popup window with the "inline" creation form is opened.

The popup window isn't much different from your usual form handling views. The main difference is that when the form has been submitted and validated successfully, after saving the newly created object, the user is not redirected to the view's ``success_url``. Instead, a special JavaScript-only response is being sent to the browser, adding the new object to the selection in the original window and closing the popup window.

Any :class:`~django.views.generic.edit.CreateView` can be made compatible with django-addanother. When opened in a popup, the view gets appended the ``?_popup=1`` GET parameter, which is how the view knows when to respond with its special JavaScript response. This special handling is taken care of in :class:`django_addanother.views.PopupMixin`, whose usage is explained in :ref:`usage`.
