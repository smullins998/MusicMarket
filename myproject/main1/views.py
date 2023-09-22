from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from main1.static.main1.python.topartists import top_artists

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
    # Your view logic here
    template_name = f'main1/artist_templates/{artist_name.lower()}.html'
    return render(request, template_name, {'artist_name': artist_name})