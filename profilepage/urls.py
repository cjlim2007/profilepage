from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('', 
url(r'^$', 'profilepage.views.home', name='home'),
url(r'^info/$', 'profilepage.views.info', name='info'), 
url(r'^profile/$', 'profilepage.views.profile', name='profile') 
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

