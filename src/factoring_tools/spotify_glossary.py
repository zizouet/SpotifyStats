# Description: This file contains the glossary of the Spotify data.
album = "master_metadata_album_album_name"
artist = "master_metadata_album_artist_name"
song = "master_metadata_track_name"
time_listened = "ms_played"
time_of_day = "ts"
skipped = "skipped"  # UNUSED/DEPRECATED

### REASON END AND RELATED VOCABULARY
reason_end = "reason_end"
reason_end_backbtn = "backbtn"
reason_end_fwdbtn = "fwdbtn"


df_cols = [
    "ms_played",
    "master_metadata_track_name",
    "master_metadata_album_album_name",
    "master_metadata_album_artist_name",
    "ts",
    "conn_country",
    "episode_name",
    "episode_show_name",
    "offline_timestamp",
    "incognito_mode",
    "ip_addr_decrypted",
    "offline",
    "platform",
    "reason_end",
    "reason_start",
    "shuffle",
    "skipped",
    "spotify_episode_uri",
    "spotify_track_uri",
    "user_agent_decrypted",
    "username",
]

df_cols_to_name = {
    time_listened: "Time listened",
    song: "Song",
    album: "Album",
    artist: "Artist",
    time_of_day: "Timestamp",
    "conn_country": "Country",
    "episode_name": "Episode Name",
    "episode_show_name": "Episode Show Name",
    "offline_timestamp": "Offline Timestamp",
    "incognito_mode": "Incognito Mode",
    "ip_addr_decrypted": "IP Address",
    "offline": "Offline",
    "platform": "Platform",
    "reason_end": "Reason End",
    "reason_start": "Reason Start",
    "shuffle": "Shuffle",
    "skipped": "Skipped",
    "spotify_episode_uri": "Spotify Episode URI",
    "spotify_track_uri": "Spotify Track URI",
    "user_agent_decrypted": "User Agent",
    "username": "Username",
}
