from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cch_backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^users/', 'restservice.views.user_list'),
    url(r'^refuels/', 'restservice.views.refuel_list'),
    url(r'^recommendations/$' , 'restservice.views.recommendations'),
    url(r'^presentation/', 'presentation.views.main'),
    url(r'^admin/', include(admin.site.urls)),
)
