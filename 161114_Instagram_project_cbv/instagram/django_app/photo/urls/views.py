from django.conf.urls import url
from .. import views

urlpatterns = [
    # url(r'^photo/$', views.photo_list, name='photo_list'),
    url(r'^photo/(?<page>[0-9]+)/$', views.PhotoList.as_view(), name='photo_list'),
]
