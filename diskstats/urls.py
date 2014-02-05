from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from diskstats import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^roots/json/$', views.fetch_roots, name='showrootsjson'),
    url(r'^dirs/json/(?P<rootdir>.+)/$', views.fetch_dirs, name='showdirsjson'),
    url(r'^dirset/json/$', views.fetch_dir_set, name='showdirsetjson'),

 #   url(r'^jobs/json/$', views.showjobsjson, name='showjobsjson'),
 #   url(r'^details/(?P<job_id>\d+)/$', views.jobdetails, name="jobdetails"),
 #   url(r'^details/json/(?P<job_id>\d+)/$', views.jobdetailsjson, name="jobdetailsjson")
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
