from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Subject(models.Model):
    class Meta:
        db_table = 'subject'

    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name


class Article(models.Model):
    class Meta:
        db_table = 'article'

    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateField()
    article_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.article_title


class Comments(models.Model):
    class Meta:
        db_table = 'comments'

    comments_text = models.TextField()
    comments_article = models.ForeignKey(Article)


class SubjectArticle(models.Model):
    class Meta:
        db_table = 'subject_article'

    article_id = models.ForeignKey(Article)
    subject_id = models.ForeignKey(Subject)
