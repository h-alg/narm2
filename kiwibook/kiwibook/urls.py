
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf.urls.defaults import * 
from kiwibook.views import *

urlpatterns = patterns('', 
(r'^kerase/$', kerase),
(r'^sabtenam/$', sabtenam),
(r'^login/$', login),
#(r'^aa/$', aa),
(r'^aa/(?P<username>.+)/$', aa),




                       

url(r'^admin/', include(admin.site.urls)),
url(r'^mydatabase/',include('mydatabase.urls')),
url(r'^mydatabase/',include(admin.site.urls)),



                    

) 