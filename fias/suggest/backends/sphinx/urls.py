from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^suggest.json$', SphinxResponseView.as_view(), name='suggest'),
    url(r'^suggest-area.json$', GetAreasListView.as_view(), name='suggest-area'),
]
