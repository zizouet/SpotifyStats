# Description: This file contains the glossary of the Spotify data.
ALBUM = "master_metadata_album_album_name"
ARTIST = "master_metadata_album_artist_name"
SONG = "master_metadata_track_name"
TIME_LISTENED = "ms_played"
TIME_OF_DAY = "ts"
SKIPPED = "skipped"  # UNUSED/DEPRECATED

### REASON END AND RELATED VOCABULARY
REASON_END = "reason_end"
REASON_END_BACKBTN = "backbtn"
REASON_END_FWDBTN = "fwdbtn"


DF_COLS = [
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

DF_COLS_TO_NAME = {
    TIME_LISTENED: "Time listened",
    SONG: "Song",
    ALBUM: "Album",
    ARTIST: "Artist",
    TIME_OF_DAY: "Timestamp",
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
