from django.http import *
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.contrib import auth
#from django.contrib.auth.forms import UserCreationForm
from blog.models import *
from loginsys.forms import UserCreationForm


def login(request):
    context = {}
    context.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            context['login_error'] = 'Неверно введены данные пользователя'
            #return redirect('loginerror.html')
            return render_to_response('login.html', context)
            #return HttpResponseRedirectBase(request, context)
    else:
        return render_to_response('login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')


def loginerror(request):
    return render_to_response('loginerror.html')


def register(request):
    context = {}

    context.update(csrf(request))
    context['form'] = UserCreationForm()
    """
    main_new_user_form = UserCreationForm()
    context['username'] = main_new_user_form['username']
    context['email'] = main_new_user_form['email']
    context['first_name'] = main_new_user_form['first_name']
    context['last_name'] = main_new_user_form['last_name']
    context['password'] = main_new_user_form['password1']
    context['password2'] = main_new_user_form['password2']
    """

    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(
                username=new_user_form.cleaned_data['username'],
                password=new_user_form.cleaned_data['password2'])
            auth.login(request,new_user)
            return redirect('/')
        else:
            #main_new_user_form = new_user_form
            context['form'] = new_user_form

    return render_to_response('register.html', context)