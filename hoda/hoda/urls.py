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
    #(r'^sabtenam/$', log),
    (r'^sabtenam/$', sabtenam),

    (r'^log/$', log),
    #(r'^aa/$', aa),
    (r'^aa/(?P<username>.+)/$', aa),
   # (r'^book/(?P<username>.+)/(?P<group>.+)/(?P<page>.+)$', book),
    (r'^book/(?P<username>.+)/(?P<group>.+)/(?P<page>.+)$', listofbook),
    (r'^proffer/(?P<username>.+)$', proffer),
    (r'^infbook/(?P<id_book>.+)$', inf_book),
    (r'^buy/(?P<username>.+)/(?P<id_book>.+)$', buy),
    (r'^endbuy/(?P<username>.+)/(?P<id_book>.+)$', endbuy),

    ###pegah
    (r'^search/$', search),
    (r'^bank/(?P<username>.+)$', bank),
    (r'^sabad/(?P<username>.+)$', sabad),
    #(r'^zeinab/$', zeinab),

    url(r'^admin/', include(admin.site.urls)),
)
