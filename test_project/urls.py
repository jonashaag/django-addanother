from django.conf.urls import url
from django.contrib import admin

from views import CreateGroup, MainView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^groups/add/$', CreateGroup.as_view(), name='add_group'),
    url(r'^$', MainView.as_view(), name='main'),
]
