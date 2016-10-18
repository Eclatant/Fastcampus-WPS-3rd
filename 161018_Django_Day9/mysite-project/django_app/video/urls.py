from django.conf.urls import url
from video import views

urlpatterns = [
    url(r'^bookmark/list/$', views.bookmark_list, name='bookmark_list'),
    url(r'^search/$', views.search, name='search'),
]
