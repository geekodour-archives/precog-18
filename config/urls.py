"""URL Configuration"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

# Third Party

urlpatterns = [
    url(r'^api/', include('memes.urls')),
    url(r'^admin/', admin.site.urls),
]

# Debug Specific URLS
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ] + urlpatterns
