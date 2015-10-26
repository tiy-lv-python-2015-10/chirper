from django.shortcuts import render
from chirp.models import Chirp


def get_chirp(request, chirp_id):
    chirp = Chirp.objects.get(pk=chirp_id)

