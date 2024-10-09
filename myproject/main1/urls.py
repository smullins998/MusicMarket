from django.urls import path
from . import views

urlpatterns = [
    # ... existing urls ...
    path('artist/<str:artist_name>/', views.artist_detail, name='artist_detail'),
    path('api/artist_metadata/', views.get_artist_metadata, name='artist_metadata'),
    path('api/artist_bio/', views.get_artist_bio, name='artist_bio'),
    path('api/artist_stock/', views.get_artist_stock, name='artist_stock'),
    path('api/artist_stock_graph/', views.get_artist_stock_graph, name='artist_stock_graph'),
    path('search/', views.search, name='search'),
    # ... existing urls ...
]