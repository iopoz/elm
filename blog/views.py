from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/base.html')
