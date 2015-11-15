from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, permissions
from rest_framework.throttling import AnonRateThrottle
from api.permissions import IsOwnerOrReadOnly

from api.serializers import ChirpSerializer, UserSerializer, FavoriteSerializer
from chirp.models import Chirp, Favorite


class SmallPagination(PageNumberPagination):
    page_size = 10


class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListCreateChirp(generics.ListCreateAPIView):
    queryset = Chirp.objects.order_by('-posted_at')
    serializer_class = ChirpSerializer
    # The pagination class will override the settings in the REST_FRAMEWORK
    pagination_class = SmallPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    throttle_scope = 'chirps'


    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def get_queryset(self):
        qs = super().get_queryset()
        username = self.request.query_params.get('username', None)
        if username:
            qs = qs.filter(author__username=username)

        keyword = self.request.query_params.get('keyword', None)
        if keyword:
            qs = qs.filter(title__icontains=keyword)
        return qs


class DetailUpdateChirp(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chirp.objects.all()
    serializer_class = ChirpSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    throttle_scope = 'chirps'


class ListCreateFavorite(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)





