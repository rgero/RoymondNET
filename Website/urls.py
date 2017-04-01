"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin

DEBUG = True

urlpatterns = [
    url(r'^', include('personal.urls')),
    url(r'^(?i)PenaltyTracker/', include('PenaltyTracker.urls'), name="ThePenaltyTracker"),
    url(r'^(?i)projects/', include('Projects.urls'), name="Projects"),
    url(r'^(?i)GuitarTrainer/', include('GuitarTrainer.urls'), name="GuitarTrainer"),
    url(r'^(?i)blog/', include('Blog.urls'), name="Blog")
]

if DEBUG == True:
    urlpatterns.append(url(r'^admin/', admin.site.urls))
