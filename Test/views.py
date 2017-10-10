from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Album
# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    # temp = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
        }
    # html = ''
    # for albums in all_albums:
    #     url ='/music/'+ str(albums.id) + '/'
    #     html +='<a href="'+ url +'">'+ albums.album_title +'</a><br>'
    # return HttpResponse(temp.render(context, request))
    return render(request, 'music/index.html', context)

def ListAlbums(request, album_id):
    
    # album = get_object_or_404(Album, pk=album_id)
    # return HttpResponse(request, 'music/details.html', {'album':album})
     try:
         album = Album.objects.get(pk=album_id)
     except Album.DoesNotExist:
         raise Http404("Album does not Exist")
     return render(request, 'music/Details.html', {'album':album})
    #  return HttpResponse("<h2> Details for Album id: " + str(album_id) +"</h2>")
