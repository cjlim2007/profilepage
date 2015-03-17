from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('', url(r'^$', 'profilepage.views.home', name='home'),url(r'^/info/$', 'buildup.views.info', name='info'), url(r'^/profile/$', 'buildup.views.profile', name='profile')) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
