
from django.urls import path
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from music import views
from django.views.generic import TemplateView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('albums/', views.AlbumList.as_view()),
    path('songs/',views.SongList.as_view()),
    path('', TemplateView.as_view(template_name='index.html')),
]

urlpatterns = format_suffix_patterns(urlpatterns)