import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

artisturi = input('Choose an artist to see their albums: ')
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(artisturi, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])

print("Poo")