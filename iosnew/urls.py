# coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings


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
    url(r'^image/(?P<path>.*)$','django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT+'/image', 'show_indexes':True}),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),


    url(r'^jeapmain$', 'jeapmain.views.home'),


    url(r'^pythonvideo$', 'pythonvideo.views.home', name='home'),
    url(r'^cates$','pythonvideo.views.cates',name='cates'),
    url(r'^courses$','pythonvideo.views.courses',name='courses'),
    url(r'^videos$','pythonvideo.views.videos',name='videos'),
    url(r'^video/(\d+)$','pythonvideo.views.video',name='video'),


    url(r'^game$', 'game.views.home', name='gamehome'),
    url(r'^list$', 'game.views.listpage', name='list'),
    url(r'^teachers$', 'game.views.teachers', name='teachres'),
    url(r'^showpage/(\d+)$', 'game.views.showpage', name='showpage'),
    url(r'^aboutus$', 'game.views.aboutus', name='aboutus'),


)
