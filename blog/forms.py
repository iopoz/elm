from django import forms
from django.forms import ModelForm
from blog.models import Comments

__author__ = 'EKravchenko'


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']