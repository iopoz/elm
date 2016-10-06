from datetime import date
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from blog.forms import CommentForm, NewArticleForm  # , NewArticleSubjectForm
from blog.models import *
from django.contrib import auth
from django.core.paginator import Paginator


def home(request, page_number=1):
    articles = Article.objects.all()
    curront_page = Paginator(list(reversed(articles)), 3)
    subjects = Subject.objects.all()
    user = auth.get_user(request).username
    context = {
        'articles': curront_page.page(page_number),
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
    context['comments'] = Comments.objects.filter(comments_article_id=article_id)
    context['form'] = comment_form['comments_text']
    context['username'] = auth.get_user(request).username

    return render(request, 'blog/article.html', context)


def addlike(request, article_id):
    if article_id in request.COOKIES:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        article = get_object_or_404(Article, id=article_id)
        article.article_likes += 1
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
    return display_article(request, article_id)#HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def newarticle(request):
    subjects = Subject.objects.all()
    user = auth.get_user(request).username
    context = {
        'subjects': subjects,
        'username': user,
    }
    if request.POST:
        new_article = NewArticleForm(request.POST)
        if new_article.is_valid():
            article = new_article.save(commit=False)
            article.article_author = request.user
            article.article_text = request.POST['description']
            article.article_title = request.POST['title']
            article.article_date = date.today()
            article.save()
            len_subj = len(request.POST.getlist('subjects'))
            if len_subj < 1:
                article.article_subject.add(subjects.get(
                    subject_name='Общее').id)
            else:
                for i in range(len_subj):
                    article.article_subject.add(subjects.get(
                        subject_name=request.POST.getlist('subjects')[i]).id)
        return redirect('/')
    return render(request, 'blog/newarticle.html', context)

