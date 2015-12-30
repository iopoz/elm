from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from blog.forms import CommentForm
from blog.models import *


def home(request):
    articles = Article.objects.all()
    subjects = Subject.objects.all()
    context = {
        'articles': articles,
        'subjects': subjects
    }
    return render(request, 'blog/home.html', context)


def about(request):
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects
    }
    return render(request, 'blog/about.html', context)

def display_article(request, article_id):
    comment_form = CommentForm(request.POST)
    context = {}
    context.update(csrf(request))
    context['article'] = get_object_or_404(Article, id=article_id)
    context['subjects'] = Subject.objects.all()
    context['comments'] = Comments.objects.filter(comments_article_id = article_id)
    context['form'] = comment_form['comments_text']

    return render(request, 'blog/article.html', context)


def addlike(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.article_likes +=1
    article.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def addcomment(request, article_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))