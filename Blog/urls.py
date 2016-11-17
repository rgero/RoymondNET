from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.blogIndex, name="blog"),
    url(r'^(?P<slug>[\w\-]+)/$', views.postView, name="postView"),
    url(r'^(?P<slug>[\w\-]+)/$', views.categories),
]
