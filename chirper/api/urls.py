from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import DetailUpdateChirp

urlpatterns = [
    url(r'^chirps/(?P<pk>\d+)', DetailUpdateChirp.as_view(), name='api_chirp_detail_update'),
    url(r'^chirps/', 'api.views.list_create_chirps'),
    url(r'^users/', 'api.views.list_users')
]

urlpatterns = format_suffix_patterns(urlpatterns)