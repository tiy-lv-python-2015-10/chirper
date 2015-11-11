from django.contrib.auth.models import User
from django.core import serializers
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import ChirpSerializer, UserSerializer
from chirp.models import Chirp
from rest_framework import generics

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

    def perform_create(self, serializer):
        serializer.save(author=User.objects.get(pk=1))

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
