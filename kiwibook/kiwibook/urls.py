
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf.urls.defaults import * 
from kiwibook.views import *

urlpatterns = patterns('', 
(r'^hello/$', hello),
(r'^sabtenam/$', sabtenam),



                       

url(r'^admin/', include(admin.site.urls)),
url(r'^mydatabase/',include('mydatabase.urls')),
url(r'^mydatabase/',include(admin.site.urls)),



                    

) 
