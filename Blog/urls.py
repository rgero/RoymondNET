from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.blogIndex, name="blog"),
    url(r'^post/(?P<slug>[\w\-]+)/$', views.postView, name="postView"),
    url(r'^categories/$', views.categoryView, name="categoryView"),
    url(r'^categories/(?P<slug>[\w\-]+)/$', views.view_category, name="categoryPostsView"),
    url(r'^tags/(?P<slug>[\w\-]+)/$', views.view_tags, name="tagPostsView"),
]
