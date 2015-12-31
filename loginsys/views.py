from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib import auth


def login(request):
    context = {}
    context.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.Post.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            context['login_error'] = '???????????? ?? ??????'
            return render_to_response('login.html', context)
    else:
        return render_to_response('login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))