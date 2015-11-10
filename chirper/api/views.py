from django.contrib.auth.models import User
from django.core import serializers
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import ChirpSerializer, UserSerializer
from chirp.models import Chirp

@api_view(['GET'])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def list_create_chirps(request):

    if request.method == "GET":
        chirps = Chirp.objects.all()
        serializer = ChirpSerializer(chirps, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        user = User.objects.get(pk=1)

        serializer = ChirpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DetailUpdateChirp(APIView):

    def get(self, request, pk, format=None):
        """
        Details about the chirp
        :param args:
        :param kwargs:
        :return:
        """
        chirp = get_object_or_404(Chirp, pk=pk)
        serializer = ChirpSerializer(chirp)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        chirp = get_object_or_404(Chirp, pk=pk)
        serializer = ChirpSerializer(chirp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        chirp = get_object_or_404(Chirp, pk=pk)
        chirp.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)