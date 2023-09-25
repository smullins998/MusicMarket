#Last FM API
import requests

api_key = 'b464441a6b577d6b83545b231ebcb168'

def lastfm_bio(artist):
    artist_name = artist

    # Define the Last.fm API endpoint for artist info
    endpoint = 'artist.getinfo'

    # Construct the request URL
    url = f'http://ws.audioscrobbler.com/2.0/?method={endpoint}&artist={artist_name}&api_key={api_key}&format=json'

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        artist_info = response.json()['artist']

        # Extract the artist's biography (truncated at 300 characters)
        bio = artist_info['bio']['content']

        # # Print the artist's biography
        # print(f"Artist Bio: {bio}")
        
    return bio