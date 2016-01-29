__author__ = 'EKravchenko'

from django.conf.urls import url, patterns
from django.contrib import admin

import blog

urlpatterns = patterns('',

                       url(r'^login/', 'loginsys.views.login', name='login'),
                       url(r'^logout/', 'loginsys.views.logout', name='logout'),
                       )

