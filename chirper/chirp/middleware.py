from django.http import HttpResponseRedirect


class SimpleMiddleware:

    def process_request(self, request):
        if 'disney' in request.GET:
            return HttpResponseRedirect('http://www.disney.com')

        return None

