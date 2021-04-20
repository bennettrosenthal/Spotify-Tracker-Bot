from TwitterAPI import TwitterAPI
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

twitterApi = TwitterAPI("API-KEY",
                 "API-SECRET",
                 "CLIENT-KEY",
                 "CLIENT-SECRET")

scope = "user-read-currently-playing user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id='LOLNO', client_secret='NOTTODAY', redirect_uri="http://localhost:8080"))

results = sp.current_playback()
print(results)
tweet = ""
currentSongString = results["item"]["name"] + " by " + results["item"]["album"]["artists"][0]["name"]
while True:
    results = sp.current_playback()
    print("\n\n")
    print(results)
    if results["currently_playing_type"] != "unknown":
        newSongString = results["item"]["name"] + " by " + results["item"]["album"]["artists"][0]["name"]
        if newSongString != currentSongString:
            currentSongString = newSongString
            tweet = "I am listening to " + currentSongString + "\n\nLink: " + results["item"]["external_urls"]["spotify"]
            r = twitterApi.request('statuses/update', {'status': tweet})
            print(tweet)
            time.sleep(10)

