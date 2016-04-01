from django.contrib import admin
from django.contrib.auth.models import User

from blog.models import Article, Comments, Subject, SubjectArticle


class CommentsInLine(admin.StackedInline):
    model = Comments
    extra = 1


class SubjectInLine(admin.StackedInline):
    model = SubjectArticle
    extra = 1


class SubjectAdmin(admin.ModelAdmin):
    fields = ['subject_name']


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date',
              'article_author']

    # inlines = [SubjectInLine]
    # inlines = [CommentsInLine]
    # list_display = (SubjectInLine,)

    inlines = [SubjectInLine, CommentsInLine]
    list_filter = ['article_date', 'article_likes', 'article_author']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Subject, SubjectAdmin)
