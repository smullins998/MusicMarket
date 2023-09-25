import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd


# Replace with your own client ID and client secret
CLIENT_ID = 'b3c21e406dc94f05a3c756b4f6f946a3'
CLIENT_SECRET = '3144ab0c08a4414a8d2dba8cf9be2999'

auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def artist_metadata(artist_name):
    
    results = sp.search(q=artist_name, type='artist')
    artist_id = results['artists']['items'][0]['id']

    response = sp.artist(artist_id)

    artist_url = response['external_urls']['spotify']
    artist_followers = response['followers']['total']

    artist_picture = response['images'][0]['url']
    artist_genres = response['genres']

    #Get track popularity metadata too
    track_metadata = sp.artist_top_tracks(artist_id)
    top_tracks = [track['name'] for track in track_metadata['tracks']]
    preview_url = [track['preview_url'] for track in track_metadata['tracks']]
    track_popularity = [track['popularity'] for track in track_metadata['tracks']]

    return dict({'url': artist_url, 'followers': artist_followers,
                 'pictures': artist_picture, 'genres': artist_genres, 'top_tracks': top_tracks,
                 'preview_url': preview_url, 'track_popularity':track_popularity})

