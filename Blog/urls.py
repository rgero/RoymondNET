from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^categories/((?P<catName>[\w\-]+))', views.category_list, name="category_list")

]
