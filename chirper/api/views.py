from django.contrib.auth.models import User
from django.core import serializers
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from chirp.models import Chirp


@csrf_exempt
def list_create_chirps(request):

    if request.method == "GET":
        chirps = Chirp.objects.all()
        response = HttpResponse(serializers.serialize("json", chirps),
                                content_type="application/json")
        return response

    elif request.method == "POST":
        user = User.objects.get(pk=1)

        data = json.loads(request.body.decodes("UTF-8"))
        chirp = Chirp.objects.create(message=request['message'],
                                     title=request['title'],
                                     author=user, posted_at=timezone.now())
        return HttpResponse(serializers.serialize("json", [chirp]),
                            status=201, content_type="application/json")


class DetailUpdateChirp(View):

    def get(self, *args, **kwargs):
        chirp = get_object_or_404(self.request.kwargs['chirp_id'])

        response = HttpResponse(serializers.serialize("json", [chirp]),
                                status=200, content_type="application/json")
        return response

    def put(self, *args, **kwargs):
        chirp = get_object_or_404(self.request.kwargs['chirp_id'])

        data = json.loads(self.request.body.decode("utf-8"))
        chirp.message = data.get('message', chirp.message)
        chirp.title = data.get('title', chirp.title)
        chirp.save()

        response = HttpResponse(serializers.serialize("json", [chirp]),
                                status=200, content_type="application/json")
        return response

    def delete(self, *args, **kwargs):
        chirp = get_object_or_404(self.request.kwargs['chirp_id'])
        chirp.delete()

        return HttpResponse([], status=204)