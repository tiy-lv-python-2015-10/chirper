from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import DetailUpdateChirp

urlpatterns = [
    url(r'^chirps/(?P<pk>\d+)/', DetailUpdateChirp.as_view()),
    url(r'^chirps/', 'api.views.list_create_chirps'),
]
urlpatterns = format_suffix_patterns(urlpatterns)