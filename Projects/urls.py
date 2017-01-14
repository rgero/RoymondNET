from django.conf.urls import url, include
from . import views
import PenaltyTracker

urlpatterns = [
    url(r'^$', views.projects, name="projects"),
    url(r'^(?i)python$', views.python, name="python"),
    url(r'^(?i)python/guitar-notes$', views.python_guitar_notes, name="python_guitar_notes"),
    url(r'^(?i)c-sharp$', views.csharp, name="c-sharp"),
    url(r'^(?i)c-sharp/selina-no$', views.csharp_selina, name="csharp-selina"),
    url(r'^(?i)c-sharp/painbow-road$', views.csharp_painbow, name="csharp-painbow"),
    url(r'^(?i)java$', views.java, name="java"),
    url(r'^(?i)java/background$', views.java_background, name="java_background"),
    url(r'^(?i)java/imageprocessor$', views.java_image_processor, name="java_image_processor"),
    url(r'^(?i)java/guitar_trainer$', views.java_guitar_trainer, name="java_guitar_trainer"),
    url(r'^(?i)perl$', views.perl, name="perl"),
    url(r'^(?i)android$', views.android, name="android"),
    url(r'^(?i)ios$', views.iOS, name="iOS"),
]
