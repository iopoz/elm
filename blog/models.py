from django.contrib.auth.models import User
from django.db import models


# Create your models here.
TEXT_LEN = 1000

class Subject(models.Model):
    class Meta:
        db_table = 'subject'

    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name


class Article(models.Model):
    article_title = models.CharField(blank=True, null=True, max_length=200)
    article_text = models.TextField(blank=True, null=True,)
    article_date = models.DateField(blank=True, null=True,)
    article_likes = models.IntegerField(default=0, blank=True, null=True)
    article_author = models.ForeignKey(User)
    article_subject = models.ManyToManyField(Subject)
    class Meta:
        db_table = 'article'

    def __str__(self):
        return self.article_title

    def get_short_text(self):
        if len(self.article_text)>TEXT_LEN:
            return self.article_text[:TEXT_LEN]
        else:
            return self.article_text


class Comments(models.Model):
    class Meta:
        db_table = 'comments'

    comments_text = models.TextField(verbose_name="Текст комментария")
    comments_article = models.ForeignKey(Article)


# class SubjectArticle(models.Model):
#     class Meta:
#         db_table = 'subject_article'
#
#     article_id = models.ForeignKey(Article)
#     subject_id = models.ForeignKey(Subject)
