from django.conf.urls import url, include
from . import views
import PenaltyTracker

urlpatterns = [
    url(r'^$', views.projects, name="projects"),

    #Python
    url(r'^(?i)python$', views.python, name="python"),
    url(r'^(?i)python/guitar-notes$', views.python_guitar_notes, name="python_guitar_notes"),
    url(r'^(?i)python/roymondnet$', views.roymond_net, name="roymond_net"),
    url(r'^(?i)python/ip_notifier$', views.python_ip_notifier, name="python_ip_notifier"),
    url(r'^(?i)python/last_to_spotify$', views.python_last_to_spotify, name="python_last_to_spotify"),

    #C-Sharp
    url(r'^(?i)c-sharp$', views.csharp, name="c-sharp"),
    url(r'^(?i)c-sharp/selina-no$', views.csharp_selina, name="csharp-selina"),
    url(r'^(?i)c-sharp/painbow-road$', views.csharp_painbow, name="csharp-painbow"),
    url(r'^(?i)c-sharp/file-renamer$', views.csharp_file_renamer, name="csharp_file_renamer"),
    url(r'^(?i)c-sharp/laser-defender$',views.csharp_laser_defender, name="csharp_laser_defender"),

    #Java
    url(r'^(?i)java$', views.java, name="java"),
    url(r'^(?i)java/background_old$', views.java_background_old, name="java_background_old"),
    url(r'^(?i)java/background$', views.java_background, name="java_background"),
    url(r'^(?i)java/imageprocessor$', views.java_image_processor, name="java_image_processor"),
    url(r'^(?i)java/guitar_trainer$', views.java_guitar_trainer, name="java_guitar_trainer"),
    url(r'^(?i)java/chord_drawer$', views.java_chord_drawer, name="java_chord_drawer"),

    #Perl
    url(r'^(?i)perl$', views.perl, name="perl"),
    url(r'^(?i)perl/size_comparsion$', views.perl_size_comparsion, name="perl_size_comparsion"),

    url(r'^(?i)android$', views.android, name="android"),
    url(r'^(?i)ios$', views.iOS, name="iOS"),
    url(r'^(?i)android/hikers_watch$', views.hikers_watch, name="android_hikers_watch"),
    url(r'^(?i)ios/hikers_watch$', views.hikers_watch, name="ios_hikers_watch"),
    url(r'^(?i)android/shooting_time$', views.shooting_time, name="android_shooting_time"),
    url(r'^(?i)ios/shooting_time$', views.shooting_time, name="ios_shooting_time"),
    url(r'^(?i)ios/guitar_trainer$', views.ios_guitar_trainer, name="ios_guitar_trainer"),

    #Javascript
    url(r'^(?i)javascript$', views.js, name="js_index"),
    url(r'^(?i)javascript/guitar-trainer$', views.js_guitar_trainer, name="js_guitar_trainer"),


    url(r'^(?i)example$', views.example_json, name="Example")
]
