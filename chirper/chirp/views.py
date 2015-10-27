from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import response
from chirp.models import Chirp


def list_chirps(request):

    chirps = get_list_or_404(Chirp)


    return render(request, 'chirp/chirp_list.html', {'chirps': chirps})

def chirp_detail(request, chirp_id):
    chirp = get_object_or_404(Chirp, pk=chirp_id)
    request.session['mytest'] = 'Happy Halloween'
    return render(request, 'chirp/chirp_detail.html', {'chirp':chirp})

