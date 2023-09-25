from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from main1.static.main1.python.topartists import top_artists
from main1.static.main1.python.artist_metadata import artist_metadata
from main1.static.main1.python.lastfm_artistbio import lastfm_bio

# Create your views here. Here are where all of the pages are

def home(response):
    return render(response, 'main1/home.html', {})


def get_top_artists(request):
    query = request.GET.get('query', '')
    if query:
        artists_data = top_artists(query)
        return JsonResponse(artists_data, safe=False)
    else:
        return JsonResponse([], safe=False)
    
def artist_detail(request, artist_name):
    # Pass the artist_data to the artist_detail.html template
    return render(request, 'main1/artists.html')


def get_artist_metadata(request):
    query = request.GET.get('query', '')
    if query:
        artists_data = artist_metadata(query)
        return JsonResponse({'artists_data': artists_data})
    else:
        return JsonResponse({'artists_data': []})
    
def get_artist_bio(request):
    query = request.GET.get('query', '')
    if query:
        bio = lastfm_bio(query)
        return JsonResponse({'bio': bio})
    else:
        return JsonResponse({'artists_data': []})
        