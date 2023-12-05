import sys
import spotipy
import configparser
from spotipy.oauth2 import SpotifyOAuth
import random

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read('config.ini')

# Get Spotify credentials
client_id = config.get('Spotify', 'client_id')
client_secret = config.get('Spotify', 'client_secret')
redirect_uri = config.get('Spotify', 'redirect_uri')
scope = config.get('Spotify', 'scope')

# Set up SpotifyOAuth
sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)

# Function to refresh the access token
def refresh_token():
    token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
    sp = spotipy.Spotify(auth=token_info['access_token'])
    return sp, token_info

# Check if token info is already saved
token_info = sp_oauth.get_cached_token()

# Check if the token_info is None or if the 'access_token' key is not present
if token_info is None or 'access_token' not in token_info:
    # If no token info is saved or if loading fails, go through the authorization process
    auth_url = sp_oauth.get_authorize_url()
    print(f'Please authorize the application by visiting this URL: {auth_url}')
    response = input('Paste the URL you were redirected to: ')
    code = sp_oauth.parse_response_code(response)
    token_info = sp_oauth.get_access_token(code)

    # Save the token info to a file for future use
    sp_oauth._save_token_info(token_info)

# Check if the token_info is None or if the 'access_token' key is not present
if token_info is None or 'access_token' not in token_info:
    print("Failed to obtain the access token.")
else:
    # Check if the token is expired
    if sp_oauth.is_token_expired(token_info):
        # If expired, refresh the token
        sp, token_info = refresh_token()

    # Get a list of available devices and authorize access for this session
    sp = spotipy.Spotify(auth=token_info['access_token'])
    devices = sp.devices()
    
# Extract device name and command from command line arguments
    if len(sys.argv) < 3:
        print("Usage: python3 spotify-api-controller.py DEVICE_NAME <play, pause>")
        sys.exit(1)

    device_name = sys.argv[1]
    command = sys.argv[2]
    # Set the playlist if the argument is provided in the commandline
    playlist_uri = None
    

    # Find the device ID for the specified device name
    device_id = None
    for device in devices['devices']:
        if device['name'] == device_name:
            device_id = device['id']
            break

    if device_id is None:
        print(f"Device with name '{device_name}' not found.")
        sys.exit(1)

    # Perform the specified command (play or pause) on the specified device
    if command == 'play':
        sp.transfer_playback(device_id=device_id, force_play=1)
        # Set it to repeat the track
        sp.repeat('context', device_id=device_id)
        print(f"Playback started on device: {device_name}")
    elif command == 'pause':
        sp.pause_playback()
        sp.transfer_playback(device_id=device_id, force_play=0)
        print(f"Playback paused on device: {device_name}")
    else:
        print("Invalid command. Please use 'play' or 'pause'.")

    if len(sys.argv) >= 4:
        # Get the playlist
        playlist_uri = sys.argv[3]
        # Shuffle the playlist
        sp.shuffle(state=True, device_id=device_id)
        sp.start_playback(uris=playlist_uri)
