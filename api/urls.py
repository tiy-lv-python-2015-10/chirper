from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import DetailUpdateChirp, ListUsers, ListCreateChirp, \
    ListCreateFavorite
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^chirps/(?P<pk>\d+)', DetailUpdateChirp.as_view(), name='api_chirp_detail_update'),
    url(r'^chirps/', ListCreateChirp.as_view(), name='api_chirp_list_create'),
    url(r'^users/', ListUsers.as_view(), name='api_user_list'),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^favorites/', ListCreateFavorite.as_view(),
        name='api_favorite_list_create')
]

urlpatterns = format_suffix_patterns(urlpatterns)