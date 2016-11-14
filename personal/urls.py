"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views
import PenaltyTracker

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^about.html', views.about, name="about"),
    url(r'^(?i)projects.html', views.projects, name="projects"),
    url(r'^(?i)projects/c-sharp', views.comingsoonprojects, name="c-sharp"),
    url(r'^(?i)projects/python', views.comingsoonprojects, name="python"),
    url(r'^(?i)projects/java', views.comingsoonprojects, name="java"),
    url(r'^(?i)projects/perl', views.comingsoonprojects, name="perl"),
    url(r'^(?i)projects/android', views.comingsoonprojects, name="android"),
    url(r'^(?i)projects/ios', views.comingsoonprojects, name="ios"),
    url(r'comingsoon.html', views.comingsoon, name="comingsoon"),
]

# Personal is the main page.
