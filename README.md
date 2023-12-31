# Spotify-API-Controller
This Python script allows you to control Spotify playback on a specific device using the Spotify API.

## Prerequisites

This script only works if the account that is used is a Spotify Premium account.

Before running the script, make sure you have the following installed on your device:

1. **Python**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **pip**: The package installer for Python. It is usually included with Python installations. If not, you can install it following the instructions [here](https://pip.pypa.io/en/stable/installation/).

## Dependencies

To install the required dependencies, run the following command in your terminal or command prompt:

```bash
pip install spotipy
```

## Configuration
1. Obtain Spotify API credentials:
  - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
  - Create a new application to get your `client_id` and `client_secret`.
  - Set the redirect_uri to `http://localhost:8888/callback`, or something else if you know what you're doing.
  - Select "Web API" in APIs used
2. Open the config.ini file and replace the placeholders with your Spotify API credentials:
```ini
client_id = your_client_id
client_secret = your_client_secret
redirect_uri = http://localhost:8888/callback
```
Don't change the scope unless you make modifications to the file that require an expanded scope.

## Usage
1. Run the script using the following command:

```bash
python spotify-api-controller.py DEVICE_NAME <play, pause> <Playlist_URI>
```
Replace `DEVICE_NAME` with the name of your Spotify device and `<play, pause>` with the desired command.
Only use the `Playlist_URI` if you are going to be **PLAYING** the playlist; you cannot set the playlist while playback is paused. It will start playback even if you enter the command with "pause".

2. If it's your first time running the script, follow the authorization prompts and paste the redirected URL when prompted.

## Notes
- If you encounter any issues or errors, make sure your Spotify API credentials are correctly configured, and your device is connected to Spotify.
- Make sure to replace placeholders like `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` with the actual values from your Spotify Developer Dashboard. Users can follow the instructions in this `README.md` to set up and run your Spotify API controller program.
