from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="projects"),
    url(r'^(?i)(?P<language>(\w*\d*)$)', views.languageHistory, name='languageHistory'),
    url(r'^(?i)(?P<language>(\w*\d*))/(?P<projectName>(\w*\d*)$)', views.projectPage, name='projectPage')
]
