import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone
from django.views.generic import View, ListView, DetailView, CreateView
from chirp.forms import ChirpForm
from chirp.models import Chirp, Tag

logger = logging.getLogger(__name__)

class ListChirps(ListView):
    model = Chirp
    queryset = Chirp.objects.order_by('-posted_at')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['page_load'] = timezone.now()
        context['tag_list'] = tags
        logger.debug('******* SOMEONE WANTS THEM SOME CHIRPS ************')
        return context


class ChirpDetail(DetailView):
    model = Chirp


class CreateChirp(CreateView):
    model = Chirp
    form_class = ChirpForm
    success_url = reverse_lazy('list_chirps')
    template_name = 'chirp/chirp_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateChirp, self).form_valid(form)

