from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="guitartrainer"),
    url(r'^index2.html', views.index2, name="tempGuitarTrainer")
]
