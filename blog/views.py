from datetime import date
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from blog.forms import CommentForm, NewArticleForm  # , NewArticleSubjectForm
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
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def newarticle(request):
    subjects = Subject.objects.all()
    user = auth.get_user(request).username

    # subject_for_article = NewArticleSubjectForm(request.POST)
    # sa = SubjectArticle.objects.all()
    context = {
        'subjects': subjects,
        'username': user,
    }
    if request.POST:
        new_article = NewArticleForm(request.POST)
        # if new_article.is_valid():
        # if new_article.is_valid():
        # new_article.save(commit=False)
        # new_article.article_title = request.POST['title']
        # new_article.article_text = request.POST['description']
        # new_article.article_date = date.today()
        # new_article.article_author = User
        if new_article.is_valid():
            article = new_article.save(commit=False)
            article.article_author = request.user
            article.article_text = request.POST['description']
            article.article_title = request.POST['title']
            article.article_date = date.today()
            article.save()
            for i in range(len(request.POST.getlist('subjects'))):
                article.article_subject.add(subjects.get(
                    subject_name=request.POST.getlist('subjects')[i]).id)

        # subject_for_article.fields.subject_id.add(1)
        # sa.subject_id.add(1)


        # form.article_author_id = auth.get_user(request).id
        # form.article_date = date.today()
        # new_article.save()
        # new_article.article_subject.add(request.POST['subjects'])

        request.session.set_expiry(60)
        request.session['pause'] = True
    return render(request, 'blog/newarticle.html', context)
    # posts = AddNewEvent
    # context = {}
    # context['EventsMod'] = AddNewEvent
    # context.update(csrf(request))
    # if request.POST:
    #     new_event = AddNewEvent(request.POST, request.FILES)
    #     new_event.title = request.POST['title']
    #     new_event.description = request.POST['description']
    #     new_event.location = request.POST['location']
    #     new_event.image = request.FILES['image']
    #     new_event.start_time = request.POST['start_time']
    #     new_event.start_date = request.POST['start_date']
    #     new_event.save()
    #     return redirect('post_list')
    # return render(request, 'blog/newarticle.html', context)
