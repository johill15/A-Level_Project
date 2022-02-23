import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
#todo: Fill in details of functions

def artistalbums():
    """
    shows the albums from the artist that is chosen
    :return: the albums of the artist
    """
    artisturi = input('Choose an artist to see their albums: ')
    results = spotify.artist_albums(artisturi, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
         print(album['name'])


def artistrelated():
    """
    shows the related artists from the chosen artist
    :return: the related artist
    """
    artisturi = input('Choose an artist to see their related artists: ')
    relatedartist = spotify.artist_related_artists(artisturi)
    print(relatedartist)


artistrelated()