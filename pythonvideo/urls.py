from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pythonvideo.views.home', name='home'),
    url(r'^cates$','pythonvideo.views.cates',name='cates'),
    url(r'^courses$','pythonvideo.views.courses',name='courses'),
    url(r'^videos$','pythonvideo.views.videos',name='videos'),
    url(r'^video/(\d+)$','pythonvideo.views.video',name='video'),
    url(r'^image/(?P<path>.*)$','django.views.static.serve',
        	{'document_root': settings.MEDIA_ROOT+'/image', 'show_indexes':True}),

    # url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT , 'show_indexes':True}),

    url(r'^admin/', include(admin.site.urls)),
)
