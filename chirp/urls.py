from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from chirp.views import ListChirps, ChirpDetail, CreateChirp

# Note that the as_view() has to be called to convert a CBV to a normal view
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^$', ListChirps.as_view(), name='list_chirps'),
    url(r'^(?P<pk>\d+)/$', ChirpDetail.as_view(),
        name='chirp_detail'),
    # View based caching
    # url(r'^(?P<pk>\d+)/$', cache_page(60)(ChirpDetail.as_view()),
    #     name='chirp_detail'),
    url(r'^create/$', login_required(CreateChirp.as_view()), name='chirp_create'),
]
