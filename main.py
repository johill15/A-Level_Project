import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def artistalbums():
    artisturi = input('Choose an artist to see their albums: ')
    results = spotify.artist_albums(artisturi, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
         print(album['name'])


def artistrelated():
    artisturi = input('Choose an artist to see their related artists: ')
    relatedartist = spotify.artist_related_artists(artisturi)
    print(relatedartist)
artistalbums()
