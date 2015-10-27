from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'chirp.views.list_chirps', name='list_chirps'),
    url(r'^(?P<chirp_id>\d+)/$', 'chirp.views.chirp_detail', name='chirp_detail')
]