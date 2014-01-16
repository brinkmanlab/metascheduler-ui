from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from webui import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^jobs/$', views.showjobs, name='showjobs'),
    url(r'^jobs/json/$', views.showjobsjson, name='showjobsjson'),
    url(r'^details/(?P<job_id>\d+)/$', views.jobdetails, name="jobdetails"),
    url(r'^details/json/(?P<job_id>\d+)/$', views.jobdetailsjson, name="jobdetailsjson")
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
