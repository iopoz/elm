from django.contrib import admin

from blog.models import Article, Comments


class ArticleInLine(admin.StackedInline):
    model = Comments
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date']
    inlines = [ArticleInLine]
    list_filter = ['article_date', 'article_likes']

admin.site.register(Article, ArticleAdmin)

