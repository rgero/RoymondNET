from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.blogIndex, name="blog"),
]