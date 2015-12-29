from django.conf.urls import url, patterns
from django.contrib import admin

import blog

urlpatterns = patterns('',
                       url(r'^$', 'blog.views.home', name='home'),
                       url(r'^about/$', 'blog.views.about', name='about'),
                       )
