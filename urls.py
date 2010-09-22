from django.conf.urls.defaults import *
from django.contrib import admin
import os

PATH = os.path.dirname(__file__)
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^codont/', include('codont.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

	#(r'^rosetta/', include('rosetta.urls')),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(PATH, "static") }),

	(r'^favicon.ico', 'django.views.static.serve',
        {'document_root': os.path.join(PATH, "static") }),
    # Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),
    
    (r'^(.*)',  include(admin.site.urls)),
)
