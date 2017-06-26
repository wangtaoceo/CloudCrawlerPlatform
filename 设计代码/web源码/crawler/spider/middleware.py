from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
from django.core.urlresolvers import reverse


class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path != reverse('register') and request.path != reverse('login'):
            username = request.session.get('username',False)
            if username:
                pass
            else:
                return HttpResponseRedirect(reverse('login'))

    def process_response(self, request, response):
        return response