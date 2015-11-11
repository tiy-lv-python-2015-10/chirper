from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import ListUsers, ListCreateChirp, DetailUpdateDeleteChirp

urlpatterns = [
    url(r'^chirps/(?P<pk>\d+)', DetailUpdateDeleteChirp.as_view(), name='api_chirp_detail_update'),
    url(r'^chirps/', ListCreateChirp.as_view()),
    url(r'^users/', ListUsers.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)