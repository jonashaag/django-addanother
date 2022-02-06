try:
    from django.conf.urls import url as re_path
except ImportError:
    from django.conf.urls import re_path
from django.contrib import admin
from testapp.views import CreateTeam, EditTeam, main

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'^team/add/$', CreateTeam.as_view(), name='add_team'),
    path(r'^team/edit/(?P<pk>.*)/$', EditTeam.as_view(), name='edit_team'),
    path(r'^$', main, name='main'),
]
