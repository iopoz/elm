from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    class Meta():
        db_table = 'article'
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateField()
    article_likes = models.IntegerField(default=0)
    #article_user = models.ForeignKey(User)
    def __str__(self):
        return self.article_title

class Comments(models.Model):
    class Meta():
        db_table = 'comments'
    comments_text = models.TextField()
    comments_article = models.ForeignKey(Article)
