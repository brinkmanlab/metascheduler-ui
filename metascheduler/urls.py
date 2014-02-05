from django.conf.urls import patterns, include, url
import settings.env

#from django.contrib import admin
#admin.autodiscover()

if settings.env.DEV_ENV:
    urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'metascheduler.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
        url(r'^metascheduler/', include('webui.urls')),
        url(r'^diskstats/', include('diskstats.urls'))
    )
else:
    urlpatterns = patterns('',
        url(r'^', include('webui.urls')),
        url(r'^diskstats/', include('diskstats.urls')),
    )

