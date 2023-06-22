import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Function to get all tracks from a Spotify playlist
def get_playlist_tracks(uri):
    results = sp.playlist_tracks(uri)  # Get the first batch of tracks
    tracks = results['items']  # Add the tracks to our list
    while results['next']:  # While there are more tracks to be fetched
        results = sp.next(results)  # Fetch the next batch of tracks
        tracks.extend(results['items'])  # Add these tracks to our list
    return tracks  # Return the complete list of tracks

# Set up Spotify API client
## Redacted client information for privacy
client_cred = SpotifyClientCredentials(client_id = 'redacted', client_secret = 'redacted')
sp = spotipy.Spotify(client_credentials_manager= client_cred)

# Specify the Spotify playlist
playlist = 'https://open.spotify.com/playlist/5RWae3GdDIEMTJ4jOHTCb5?si=e21e054876684183'
URI = playlist.split('/')[-1].split('?')[0]  # Extract the playlist URI from the playlist URL

# Fetch all tracks from the playlist
data = get_playlist_tracks(URI)

# Process each track
updated_playlist = []
for row in data:
    # Extract relevant information from each track
    track_id = row['track']['id']
    track_name = row['track']['name']
    artist = [artist['name'] for artist in row['track']['artists']]
    track_length = row['track']['duration_ms']
    track_popularity = row['track']['popularity']
    track_added = row['added_at']
    album_id = row['track']['album']['id']
    album_name = row['track']['album']['name']
    total_album_tracks = row['track']['album']['total_tracks']
    album_release_date = row['track']['album']['release_date']
    track_url = row['track']['external_urls']['spotify']
    album_url = row['track']['album']['external_urls']['spotify']

    # Append this information as a dictionary to list
    updated_playlist.append({
        'track_id': track_id,
        'track_name': track_name,
        'artist': artist,
        'track_length': track_length,
        'track_popularity': track_popularity, 
        'track_added': track_added,
        'album_id': album_id,
        'album_name': album_name,
        'total_album_tracks': total_album_tracks,
        'album_release_date': album_release_date,
        'track_url': track_url,
        'album_url': album_url
    })

# Convert dictionary to pd df
spotify_df = pd.DataFrame.from_dict(updated_playlist)

# Remove brackets from artist column
spotify_df['artist'] = spotify_df['artist'].str.join(', ')

# Convert release_date to datetime, extract year, and rename column
spotify_df['album_release_year'] = pd.to_datetime(spotify_df['album_release_date']).dt.year
spotify_df.drop('album_release_date', axis=1, inplace=True)

# Convert track_added to date_time variable type
spotify_df['track_added'] = pd.to_datetime(spotify_df['track_added'])

# Convert track_length from milliseconds to minutes and seconds (m.ss)
spotify_df['track_length'] = spotify_df['track_length'] / 60000 

# Export df to a csv file
spotify_df.to_csv("Spotify_Playlist.csv")