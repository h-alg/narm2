
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf.urls.defaults import * 
from kiwibook.views import *


#####test zeinaaaaaaaaaaab
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = patterns('', 
(r'^kerase/$', kerase),
(r'^sabtenam/$', sabtenam),
(r'^login/$', login),
#(r'^aa/$', aa),
(r'^aa/(?P<username>.+)/$', aa),
(r'^book/(?P<username>.+)/(?P<group>.+)/(?P<page>.+)$', book),
(r'^proffer/(?P<username>.+)$', proffer),
(r'^infbook/(?P<id_book>.+)$', inf_book),

###pegah
(r'^search/(?P<username>.+)/$', search),                       





                       

url(r'^admin/', include(admin.site.urls)),
url(r'^mydatabase/',include('mydatabase.urls')),
url(r'^mydatabase/',include(admin.site.urls)),



                    

) 
