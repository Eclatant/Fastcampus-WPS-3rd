from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]