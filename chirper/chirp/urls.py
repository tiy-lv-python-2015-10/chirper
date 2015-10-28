from django.conf.urls import url
from chirp.views import ListChirps

# Note that the as_view() has to be called to convert a CBV to a normal view
urlpatterns = [
    url(r'^$', ListChirps.as_view(), name='list_chirps'),
    url(r'^(?P<chirp_id>\d+)/$', 'chirp.views.chirp_detail',
        name='chirp_detail'),
    url(r'^create/$', 'chirp.views.chirp_create', name='chirp_create')
]
