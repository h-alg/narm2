from django.contrib import admin
from django.conf.urls import *


from pegah.views import *

admin.autodiscover()
urlpatterns = patterns('',

('^$',search_book),

url(r'^search_book/$',search_book),
url(r'^search/$',search),
url(r'^admin/', include(admin.site.urls)),


)