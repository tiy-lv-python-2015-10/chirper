from django.conf.urls import url
from api.views import DetailUpdateChirp

urlpatterns = [
    url(r'^chirps/', 'api.views.list_create_chirps'),
    url(r'^chirps/(?P<chirp_id>\d+)/', DetailUpdateChirp.as_view()),
]
