from django.conf.urls.defaults import patterns, include, url
from cms.sitemaps import CMSSitemap

urlpatterns = patterns('',
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^blog/', include('zinnia.urls')),
    url(r'^', include('cms.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
)
