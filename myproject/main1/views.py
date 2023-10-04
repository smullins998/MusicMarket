from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from main1.static.main1.python.topartists import top_artists
from main1.static.main1.python.artist_metadata import artist_metadata
from main1.static.main1.python.lastfm_artistbio import lastfm_bio
from .forms import OrderSubmit
from django.contrib.auth.decorators import login_required

# from .forms import Register

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
 
@login_required   
def artist_detail(request, artist_name):
    if request.method == 'POST':
        print("Received a POST request")
        form = OrderSubmit(request.POST)
        if form.is_valid():
            print("Form is valid")      
            print(form.cleaned_data)
        else:
            print('invalid form')
            
        return redirect(request.path)
        
    else:
        print("Received a GET request")
        form = OrderSubmit()
    
    return render(request, 'main1/artists.html', {'form': form})

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
    
@login_required
def trade(request):
    return render(request, 'main1/trade.html')
