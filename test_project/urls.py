from django.conf.urls import url
from django.contrib import admin

from views import AddView, FormView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add/$', AddView.as_view(), name='add'),
    url(r'^$', FormView.as_view(), name='form'),
]
