from django.conf.urls import url
from video.views.bookmark import bookmark_list, add_bookmark

urlpatterns = [
    url(r'^search/$', views.search, name='search'),
]
