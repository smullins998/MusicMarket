from django.shortcuts import render, get_object_or_404
from .models import Artist

def home(request):
    # Add your home view logic here
    return render(request, 'main1/home.html')

def get_top_artists(request):
    # Add your API logic for top artists here
    pass

def artist_detail(request, artist_name):
    artist = get_object_or_404(Artist, name=artist_name)
    return render(request, 'main1/artist_detail.html', {'artist': artist})