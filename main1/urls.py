from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/top_artists/', views.get_top_artists, name='get_top_artists'),
    path('artist/<str:artist_name>/', views.artist_detail, name='artist_detail'),
]