
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#urlpatterns = ...

#urlpatterns += staticfiles_urlpatterns()
from . import views

app_name = 'music'

urlpatterns = [ 
    url(r'^$' , views.index, name='index'),
    #/music/712/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail , name = 'detail') ,	

   	url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite , name = 'favorite') ,
]