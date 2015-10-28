from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import View
from chirp.forms import ChirpForm
from chirp.models import Chirp


def list_chirps(request):
    """
    Function based view to get a list of chirps.  Will raise 404 on empty list
    :param request:
    :return:
    """
    chirps = get_list_or_404(Chirp)
    return render(request, 'chirp/chirp_list.html', {'chirps': chirps})


class ListChirps(View):
    """
    Class version of manually get the list of chirps
    """
    def get(self, request):
        chirps = get_list_or_404(Chirp)
        return render(self.request, 'chirp/chirp_list.html', {'chirps': chirps})


def chirp_detail(request, chirp_id):
    """
    Detailed view of chirp.  Will raise 404 on missing model
    :param request:
    :param chirp_id:
    :return:
    """
    chirp = get_object_or_404(Chirp, pk=chirp_id)

    return render(request, 'chirp/chirp_detail.html', {'chirp': chirp})

def chirp_create(request):
    """
    Creates a chirp in a function based method
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = ChirpForm(request.POST)

        if form.is_valid():
            chirp = form.save(commit=False)
            chirp.author = request.user
            chirp.save()

            return HttpResponseRedirect(reverse('list_chirps'))
    else:
        form = ChirpForm()

    return render(request, 'chirp/chirp_create.html', {'form': form})

class CreateChirp(View):
    """
    Class for creating a new chirp
    """

    def get(self, request):
        """
        Handles the get request that returns a blank chirp form
        :param request:
        :return:
        """
        form = ChirpForm()
        return render(request, 'chirp/chirp_create.html', {'form': form})

    def post(self, *args, **kwargs):
        form = ChirpForm(self.request.POST)

        if form.is_valid():
            chirp = form.save(commit=False)
            chirp.author = self.request.user
            chirp.save()

            return HttpResponseRedirect(reverse('list_chirps'))

        return render(self.request, 'chirp/chirp_create.html', {'form': form})