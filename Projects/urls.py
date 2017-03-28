from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="projects"),
    url(r'^(?i)(?P<language>[^\/]*$)', views.languageHistory, name='languageHistory'),
    url(r'^(?i)(?P<language>[^\/]*)/(?P<slug>[^\/]*$)', views.projectPage, name='projectPage')
]
