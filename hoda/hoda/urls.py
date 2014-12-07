from django.conf.urls import patterns, include, url
from django.contrib import admin

from hodaapp.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hoda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^sefaresh/$', sefaresh),
     (r'^login/$', login),
     (r'^kerase/$', kerase),
    (r'^sabtenam/$', log),
    #(r'^sabtenam/$', sabtenam),

    (r'^log/$', log),
    #(r'^aa/$', aa),
    (r'^aa/(?P<username>.+)/$', aa),
    (r'^book/(?P<username>.+)/(?P<group>.+)/(?P<page>.+)$', book),
    (r'^proffer/(?P<username>.+)$', proffer),
    (r'^infbook/(?P<id_book>.+)$', inf_book),

    ###pegah
    (r'^search/$', search),

    url(r'^admin/', include(admin.site.urls)),
)
