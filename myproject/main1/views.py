from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from main1.static.main1.python.topartists import top_artists
from main1.static.main1.python.artist_metadata import artist_metadata
from main1.static.main1.python.lastfm_artistbio import lastfm_bio
from main1.static.main1.python.artist_stock import artist_stock
from main1.static.main1.python.artist_stock_graph import artist_stock_graph
from .forms import OrderSubmit
from django.contrib.auth.decorators import login_required
from datetime import datetime
import uuid
import mysql.connector
import plotly.graph_objs as go
from plotly.io import to_html
from django.shortcuts import render
from datetime import datetime
import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Artist
from django.http import JsonResponse
from django.db.models import Q

def home(response):
    return render(response, 'main1/home.html', {})

def get_top_artists(request):
    query = request.GET.get('query', '')
    if query:
        artists_data = top_artists(query)
        return JsonResponse(artists_data, safe=False)
    else:
        return JsonResponse([], safe=False)

##############
#BUYSELL FORM SUBMISSION 
##############

@login_required
def artist_detail(request, artist_name):
    # Pass only the artist name to the template
    form = OrderSubmit()
    context = {
        'artist': artist_name,
        'form': form,
    }
    return render(request, 'main1/artists.html', context)

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
        return JsonResponse({'bio': ''})

def get_artist_stock(request):
    stock = artist_stock()
    return JsonResponse({'stock': stock})

def get_artist_stock_graph(request):
    artist = request.GET.get('artist', '')
    if artist:
        stock_graph = artist_stock_graph(artist)
        return JsonResponse({'stock_graph': stock_graph})
    else:
        return JsonResponse({'stock_graph': []})

@login_required
def trade(request):
    return render(request, 'main1/trade.html')

def search(request):
    genres = Artist.objects.values_list('genre', flat=True).distinct()
    selected_genre = request.GET.get('genre', '')
    
    if selected_genre:
        top_artists = Artist.objects.filter(genre=selected_genre).order_by('-popularity')[:10]
    else:
        top_artists = Artist.objects.all().order_by('-popularity')[:10]
    
    for artist in top_artists:
        artist.stock_price = calculate_stock_price(artist)
    
    context = {
        'genres': genres,
        'selected_genre': selected_genre,
        'top_artists': top_artists,
    }
    return render(request, 'main1/search.html', context)

def calculate_stock_price(artist):
    # Implement your stock price calculation logic here
    # This is a placeholder function
    return 100.00  # Return a dummy value for now

