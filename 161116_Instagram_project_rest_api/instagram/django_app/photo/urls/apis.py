from django.conf.urls import url
from .. import apis

urlpatterns = [
    # url(r'^photo/$', apis.PhotoList.as_view(), name='photo_list'),
    url(r'^photo/$', apis.PhotoListMixinView.as_view(), name='photo_list'),
    url(r'^(?P<photo_pk>[0-9]+)/comment/add/$', apis.comment_add, name='comment_add'),
]
