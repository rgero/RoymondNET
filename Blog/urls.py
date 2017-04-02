from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name="index"),
    url(r'^(?i)categories/(?P<catName>[\w\-]+)', views.category_list, name="category_list"),
    url(r'^(?i)post/(?P<postSlug>[\w\-]+)', views.post_detail, name="post_detail")
]
