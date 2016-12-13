from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.form_test, name='penalty_index'),
]
#    url(r'^printresults/$', views.print_results, name="penalty_results"),
