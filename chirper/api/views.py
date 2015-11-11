from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from api.serializers import ChirpSerializer, UserSerializer
from chirp.models import Chirp

class SmallPages(PageNumberPagination):
    page_size = 5


class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListCreateChirp(generics.ListCreateAPIView):
    queryset = Chirp.objects.all().order_by('-posted_at')
    serializer_class = ChirpSerializer

    def perform_create(self, serializer):
        serializer.save(author=User.objects.get(pk=1))

    def get_queryset(self):
        qs = super().get_queryset()
        username = self.request.query_params.get('username', None)
        if username:
            qs = qs.filter(author__username=username)

        return qs


class DetailUpdateDeleteChirp(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChirpSerializer
    queryset = Chirp.objects.all()
