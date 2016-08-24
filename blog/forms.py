from django import forms
from django.forms import ModelForm
from blog.models import Comments, Article

__author__ = 'EKravchenko'


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']


class NewArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['article_title', 'article_text']
