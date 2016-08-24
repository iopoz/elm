from datetime import date
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from blog.forms import CommentForm, NewArticleForm
from blog.models import *
from django.contrib import auth


def home(request):
    articles = Article.objects.all()
    subjects = Subject.objects.all()
    user = auth.get_user(request).username
    context = {
        'articles': articles,
        'subjects': subjects,
        'username': user
    }
    return render(request, 'blog/home.html', context)


def about(request):
    subjects = Subject.objects.all()
    user = auth.get_user(request).username
    context = {
        'subjects': subjects,
        'username': user
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
    context['username'] = auth.get_user(request).username

    return render(request, 'blog/article.html', context)


def addlike(request, article_id):
    if article_id in request.COOKIES:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        article = get_object_or_404(Article, id=article_id)
        article.article_likes +=1
        article.save()
        response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        response.set_cookie(article_id, 'test')
        return response


def addcomment(request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def newarticle(request):
    subjects = Subject.objects.all()
    user = auth.get_user(request).username
    form = NewArticleForm(request.POST)
    context = {
        'subjects': subjects,
        'username': user,
        'form': form


    }
    if request.POST:

        if form.is_valid():
            article = form.save(commit=False)
            article.article_author_id = auth.get_user(request).id
            article.article_date = date.today()
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return render(request, 'blog/newarticle.html', context)