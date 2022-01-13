import requests
import json
import spotipy
from spotipy import SpotifyClientCredentials
from twilio.rest import Client

def get_latest_song_name():

    client_id = 'bc0aa026082c4b9b9eec8a593fde5e6c'
    client_secret = 'f026bd9ae02a48e1bc0aa68c83233a13'
    artist_id = 'https://open.spotify.com/artist/2YZyLoL8N0Wb9xBt1NhZWg?si=MDODrAaaRuqEGFnWmSAfEQ'

    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    results = spotify.artist_albums(artist_id=artist_id, album_type='single', country='ZA', limit=1, offset=0)
    return results['items'][0]['name']



def send_message(message):

    account_sid = 'AC3988f199765e116813aec161e9c09aed'
    auth_token = '211e46613cf8143b2155693cfed26e11'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_='+17156414607',
        to='+//YOUR OWN PHONE NUMBER'
    )


def main():
    if get_latest_song_name() == 'family ties (with Kendrick Lamar)':
        send_message('Has Kendrick decided to bless us today: NOO')
    else:
        send_message("Has Kendrick decided to bless us today: YEEEESSSS")



if __name__ == '__main__':
    main()

