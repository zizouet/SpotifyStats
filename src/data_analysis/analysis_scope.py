from enum import Enum

import factoring_tools.spotify_glossary as glossary


# Description: This file contains the analysis scope of the Spotify data for each function in data_analysis.py
class AnalysisScope(Enum):
    """This class contains the analysis scope of the Spotify data for each function in data_analysis.py

    Args:
        Enum (class): Enum class
    """

    MOST_LISTENED_ARTIST = [glossary.ARTIST, glossary.TIME_LISTENED]
    MOST_LISTENED_ALBUM = [glossary.TIME_LISTENED, glossary.ALBUM, glossary.ARTIST]
    MOST_LISTENED_SONG = [glossary.SONG, glossary.TIME_LISTENED, glossary.ARTIST]

    LISTENING_TIME = [glossary.TIME_LISTENED]
    LISTENING_TIME_OF_DAY = [glossary.TIME_OF_DAY, glossary.TIME_LISTENED]
    WEEKLY_BEST_SONGS = [
        glossary.TIME_OF_DAY,
        glossary.TIME_LISTENED,
        glossary.SONG,
        glossary.ARTIST,
    ]
    MOST_SKIPPED_SONGS = [glossary.SONG, glossary.ARTIST, glossary.SKIPPED]
