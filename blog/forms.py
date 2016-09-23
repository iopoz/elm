from django import forms
from django.forms import ModelForm
from blog.models import Comments, Article  # , SubjectArticle

__author__ = 'EKravchenko'


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']


class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = ['article_title', 'article_text', 'article_date',
                  'article_likes',
                  'article_author', 'article_subject']

# class NewArticleSubjectForm(forms.ModelForm):
#     class Meta:
#         model = SubjectArticle
#
#         fields = ('subject_id', 'article_id')
