from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'taskstack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('taskstack_core.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
