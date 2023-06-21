# Spotify Playlist Explorer
Spotify Playlist Explorer is a Python-based project that uses the Spotify Web API and Spotipy Python library to fetch detailed information about tracks in a specific Spotify playlist. The information is processed, cleaned, and stored in a CSV file for further exploration and analysis.

# Features
Fetches all tracks from a specific Spotify playlist and retrieves detailed information about each track:

* Track ID

* Track name

* Artist name(s)

* Track length (converted from milliseconds to minutes)

* Track popularity score

* Date when the track was added to the playlist

* Album ID

* Album name

* Number of total tracks on the album

* Album release date (year only)

* URLs for both the track and the album on Spotify

# Installation
Make sure you have Python 3.6 or later installed on your system. It would be best to have the Pandas and Spotipy Python libraries. You can install them using pip:

```python
 pip install pandas spotipy
```

# Usage 

Replace the 'client_id' and 'client_secret' fields in the SpotifyClientCredentials function with your Spotify client ID and client secret.

Replace the 'playlist' string with the URL of your desired Spotify playlist.

Run the Python script. The result will be saved in a file named "Spotify_Playlist.csv" in your current directory.

# Limitations
This script can only access public Spotify playlists. The Spotify Web API's rate limits limit the amount of data retrieved.

# Future Work
Future versions of Spotify Playlist Explorer might include the ability to handle private playlists (with the user's permission), better error handling and recovery, and more advanced data processing features.
