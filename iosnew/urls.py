# coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from .views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aka.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', mainpage),
    url(r'^mainpage/$', mainpage),
    url(r'^mainpageenglish/$', mainpageenglish),
    url(r'simple/$', simple),
    url(r'^simplechinese/$', simpleenglish),
)
