import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd


# Replace with your own client ID and client secret
CLIENT_ID = 'b3c21e406dc94f05a3c756b4f6f946a3'
CLIENT_SECRET = '3144ab0c08a4414a8d2dba8cf9be2999'

auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)



def top_artists(query):
    top_artists = []
    popularity_count = []

    # Start with an offset of 0
    offset = 0

    while len(top_artists) < 10:
        # Use Spotify's search function to search for artists whose names start with the query
        results = sp.search(q=f'artist:"{query}*"',
                            type='artist', limit=50, offset=offset)

        # Iterate through the search results
        for artist in results['artists']['items']:
            if len(top_artists) >= 10:
                break

            popularity = artist['popularity']

            # Add the artist to the list if it has popularity
            if popularity > 0:
                top_artists.append(artist['name'])

        # Increase the offset to fetch the next page of search results
        offset += 50

    return top_artists