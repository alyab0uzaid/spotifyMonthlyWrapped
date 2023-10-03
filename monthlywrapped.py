import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, url_for, session, redirect

app = Flask(__name__)

app.config['SESSION_COOKIE_NAME'] = 'Spotify Cookie'
app.secret_key = 'asfh98A%#$%lkhsfdfkjh'
TOKEN_INFO = 'token_info'

# Spotify API credentials
SPOTIPY_CLIENT_ID = "b942a9a67d25444ebce84f5150134c1e"
SPOTIPY_CLIENT_SECRET = "3269f3e727804ec5b34c72d93f842ccf"
SPOTIPY_REDIRECT_URI = "http://127.0.0.1:5000/redirect"


PLAYLIST_NAME = "Last Month's Top Songs"

@app.route('/')
def login():
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirect_page():
    session.clear()
    code = request.args.get('code')
    token_info = create_spotify_oauth().get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('save_wrapped', external=True))

@app.route('/saveWrapped')
def save_wrapped():
    try:
        token_info = get_token()
    except:
        print("User not logged in")
        return redirect('/')
    
    sp = spotipy.Spotify(auth=token_info['access_token'])
    
    # Create a new playlist with top songs
    create_playlist_with_top_songs(sp)
    
    return "Playlist created successfully!"

# Function to create a new playlist with top songs
def create_playlist_with_top_songs(sp):
    # Get the user's ID
    user_id = sp.me()['id']
    
    # Create a new playlist
    playlist = sp.user_playlist_create(user_id, PLAYLIST_NAME, public=False)
    playlist_id = playlist['id']
    
    # Get the top songs 
    top_tracks = get_top_tracks(sp)
    
    # Add the top songs to the playlist
    sp.playlist_add_items(playlist_id, top_tracks)

# Function to retrieve the access token
def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        redirect(url_for('login', external=False))

    now = int(time.time())

    is_expired = token_info['expires_at'] - now < 60
    if is_expired:
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info

# Function to create a Spotify OAuth object
def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope='playlist-modify-public playlist-modify-private user-library-read user-top-read'
    )

def get_top_tracks(sp, time_range='short_term', limit=10):
    results = sp.current_user_top_tracks(time_range=time_range, limit=limit)
    track_uris = [track['uri'] for track in results['items']]
    return track_uris

if __name__ == '__main__':
    app.run(debug=True)
