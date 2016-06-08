from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from testapp.views import CreateTeam, EditTeam, main

from django import views as django_views
urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^team/add/$', CreateTeam.as_view(), name='add_team'),
    url(r'^team/edit/(?P<pk>.*)/$', EditTeam.as_view(), name='edit_team'),
    url(r'^$', main, name='main'),
]
