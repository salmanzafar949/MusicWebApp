from django.conf.urls import url
from . import views
urlpatterns = [
    #/music/
    url(r'^$', views.index, name='index'),
    #/music/1/
    url(r'^(?P<album_id>[0-9]+)/$', views.ListAlbums, name='ListAlbums'),
    #/music/1/fav
    url(r'^(?P<album_id>[0-9]+)/fav$', views.fav, name='fav'),
]