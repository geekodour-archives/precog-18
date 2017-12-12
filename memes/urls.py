from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from memes import views

urlpatterns = [
    url(r'^memes/$', views.MemeList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)