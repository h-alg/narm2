

from django.contrib import admin
from django.conf.urls import *
admin.autodiscover()

#from django.conf.urls.defaults import *
from kiwibook.views import *
import django.contrib
django.contrib.admin.autodiscover()

#####test zeinaaaaaaaaaaab
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = patterns('',
('^$',kerase),
(r'^kerase/$', kerase),
(r'^sabtenam/$', sabtenam),
(r'^login/$', login),
#(r'^aa/$', aa),
(r'^aa/(?P<username>.+)/$', aa),
(r'^book/(?P<username>.+)/(?P<group>.+)/(?P<page>.+)$', book),
(r'^proffer/(?P<username>.+)$', proffer),
(r'^infbook/(?P<id_book>.+)$', inf_book),

###pegah
(r'^search/$', search),
(r'^sefaresh/$', sefaresh),
#(r'^thanks/$', sefaresh),







                       

url(r'^admin/', include(django.contrib.admin.site.urls)),
url(r'^mydatabase/',include('mydatabase.urls')),
url(r'^mydatabase/',include(django.contrib.admin.site.urls)),



                    

) 
