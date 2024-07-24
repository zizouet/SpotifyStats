from enum import Enum

import factoring_tools.spotify_glossary as glossary


# Description: This file contains the analysis scope of the Spotify data for each function in data_analysis.py
class AnalysisScope(Enum):
    """This class contains the analysis scope of the Spotify data for each function in data_analysis.py

    Args:
        Enum (class): Enum class
    """

    MOST_LISTENED_ARTIST = [glossary.artist, glossary.time_listened]
    MOST_LISTENED_ALBUM = [glossary.time_listened, glossary.album, glossary.artist]
    MOST_LISTENED_SONG = [glossary.song, glossary.time_listened, glossary.artist]

    LISTENING_TIME = [glossary.time_listened]
    LISTENING_TIME_OF_DAY = [glossary.time_of_day, glossary.time_listened]
    WEEKLY_BEST_SONGS = [
        glossary.time_of_day,
        glossary.time_listened,
        glossary.song,
        glossary.artist,
    ]
    MOST_SKIPPED_SONGS = [glossary.song, glossary.artist, glossary.skipped]
