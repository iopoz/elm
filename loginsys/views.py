from django.http import *
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib import auth
from blog.models import *


def login(request):
    context = {}
    context.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            context['login_error'] = 'Неверно введены данные пользователя'
            return redirect('loginerror.html')
            #return render_to_response('loginerror.html', context)
            #return HttpResponseRedirectBase(request, context)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def loginerror(request):
    return render_to_response('loginerror.html')