from django.conf.urls import url
import blog.views

urlpatterns = [
    url(r'^$', blog.views.home, name='home'),
    url(r'^about/$', blog.views.about, name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', blog.views.display_article, name='article'),
    url(r'^articles/addlike/(?P<article_id>[0-9]+)/$', blog.views.addlike, name='addlike'),
    url(r'^articles/addcomment/(?P<article_id>[0-9]+)/$', blog.views.addcomment, name='addcomment'),
]
