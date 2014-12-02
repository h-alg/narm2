from django.conf.urls import patterns, include, url
from django.contrib import admin

from hodaapp.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hoda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^sefaresh/$', sefaresh),
     (r'^login/$', login),

    url(r'^admin/', include(admin.site.urls)),
)
