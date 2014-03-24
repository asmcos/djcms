from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'game.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),



    url(r'^game$', 'game.views.home', name='home'),
    url(r'^list$', 'game.views.listpage', name='list'),
    url(r'^teachers$', 'game.views.teachers', name='teachres'),
    url(r'^showpage/(\d+)$', 'game.views.showpage', name='showpage'),
    url(r'^aboutus$', 'game.views.aboutus', name='aboutus'),
)
