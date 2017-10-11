from django.conf.urls import url
from . import views
urlpatterns = [

    ## url for clases vie genric views
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='ListAlbums')
    # #/music/
    # url(r'^$', views.index, name='index'),
    # #/music/1/
    # url(r'^(?P<album_id>[0-9]+)/$', views.ListAlbums, name='ListAlbums'),
    # #/music/1/fav
    # url(r'^(?P<album_id>[0-9]+)/fav$', views.fav, name='fav'),
]