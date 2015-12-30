from django.conf.urls import url, patterns
from django.contrib import admin

import blog

urlpatterns = patterns('',
                       url(r'^$', 'blog.views.home', name='home'),
                       url(r'^about/$', 'blog.views.about', name='about'),
                       url(r'^articles/(?P<article_id>[0-9]+)/$', 'blog.views.display_article', name='article'),
                       url(r'^articles/addlike/(?P<article_id>[0-9]+)/$', 'blog.views.addlike', name='addlike')
                       )
