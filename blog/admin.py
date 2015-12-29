from django.contrib import admin

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
    fields = ['article_title', 'article_text', 'article_date']

    #inlines = [SubjectInLine]
    #inlines = [CommentsInLine]
    '''
    fieldsets = (
        (None, {
            'fields': ('article_title', 'article_text', 'article_date', 'subject_id')
        }),
    )
    '''
    #list_display = (SubjectInLine,)

    inlines = [SubjectInLine, CommentsInLine]
    list_filter = ['article_date', 'article_likes']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Subject, SubjectAdmin)

