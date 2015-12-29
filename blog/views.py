from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response


def home(request):

    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')