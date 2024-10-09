from django.urls import path, include

from . import views

urlpatterns =  [
    path('', views.home, name='home'),
    path('api/top_artists/', views.get_top_artists, name='get_top_artists'),
    path('artist/<str:artist_name>/', views.artist_detail, name='artist_detail'),
    path('api/artist_metadata/', views.get_artist_metadata, name='artist_metadata'),
    path('api/artist_bio/', views.get_artist_bio, name='artist_bio'),
    path('api/artist_stock/', views.get_artist_stock, name='artist_stock'),
    path('api/artist_stock_graph/', views.get_artist_stock_graph, name='artist_stock_graph'),
    path('trade/', views.trade, name='trade'),


]