"""
This module contains the functions to analyze the data from Spotify.
"""

import pandas as pd

from data_analysis import analysis_scope as s
from factoring_tools import spotify_glossary as glossary
from factoring_tools import time_formatting as time_format
from report_generation import pdf_generation as pdf


def full_analysis(data, number_of_items=10):
    """
    Run the full analysis of the data and generate a pdf file with the results.

    Args:
        data (pandas df): data to analyze
        number_of_items (int, optional): number of items to output
                                         Defaults to 10.
    """
    top_artist = most_listened_artist(data, number_of_items)
    top_album = most_listened_album(data, number_of_items)
    top_song = most_listened_song(data, number_of_items)
    top_skipped_songs = most_skipped_songs(data)

    pdf.generate_pdf(
        "output/SpotifyDataAnalysis.pdf",
        most_listened_artist=top_artist,
        most_listened_album=top_album,
        most_listened_song=top_song,
        listening_time=listening_time(data),
        listening_time_of_day=listening_time_of_day(data),
        skipped_songs=top_skipped_songs,
    )


def __most_listened(data, columns, item_analyzed, number_of_items=1):
    """
    This function is a polymorphic function
    that returns the most listened artist, album, or song.

    Args:
        data (pandas df): data to analyze
        columns (data columns): minimum set of column used for running the analysis,
                                 used for optimization
        item_analyzed (data column): the column you're gonna group by with.
        number_of_items (int, optional): number of items you want to output. Defaults to 1.

    Returns:
        pandas df: output the number of items most listened songs, albums, or artists.
    """
    return (
        round(
            time_format.ms_to_hours(
                data[columns]
                .groupby(item_analyzed)
                .sum()
                .sort_values(glossary.TIME_LISTENED, ascending=False)
                .head(number_of_items)
            )
        )
        .reset_index()
        .rename(columns=glossary.DF_COLS_TO_NAME)
    )


def most_listened_artist(data, number_of_artists=1):
    """
    This function returns the most listened artists.

    Args:
        data (pandas df): data
        number_of_artists (int, optional): number of artists you want to output.
                                            Defaults to 1.

    Returns:
        pandas df: the number of items most listened artists.
    """
    return __most_listened(
        data,
        s.AnalysisScope.MOST_LISTENED_ARTIST.value,
        glossary.ARTIST,
        number_of_artists,
    )


def most_listened_album(data, number_of_albums=1):
    """
    This function returns the most listened albums.

    Args:
        data (pandas df): data
        number_of_albums (int, optional): numbers of albums you want to output.
                                         Defaults to 1.

    Returns:
        pandas df: the number of items most listened albums.
    """
    return __most_listened(
        data,
        s.AnalysisScope.MOST_LISTENED_ALBUM.value,
        [glossary.ALBUM, glossary.ARTIST],
        number_of_albums,
    ).rename(columns=glossary.DF_COLS_TO_NAME)


def most_listened_song(data, number_of_songs=1):
    """This function returns the most listened songs.

    Args:
        data (pandas df): data
        number_of_songs (int, optional): number of songs you want to output.
                                         Defaults to 1.

    Returns:
        pandas df: the number of items most listened songs.
    """
    return __most_listened(
        data,
        s.AnalysisScope.MOST_LISTENED_SONG.value,
        [glossary.SONG, glossary.ARTIST],
        number_of_songs,
    ).rename(columns=glossary.DF_COLS_TO_NAME)


def listening_time(data):
    """This function returns the total time listened to music.

    Args:
        data (pandas df): data

    Returns:
        _type_: Int
    """
    return int(round(time_format.ms_to_hours(data[glossary.TIME_LISTENED].sum())))


def listening_time_of_day(data):
    """This function returns the listening time during each hour of the day.
    E.g. : It allows you to see if you listen music more at night or during the day.

    Args:
        data (pandas df): data

    Returns:
        pandas df: array for listening time during each hour of the day.
    """
    hours = data[glossary.TIME_OF_DAY].apply(time_format.extract_hour_from_timestamp)
    return round(
        time_format.ms_to_hours(
            data[s.AnalysisScope.LISTENING_TIME_OF_DAY.value]
            .assign(hour=hours)
            .groupby("hour")
            .sum()
            .sort_values("hour", ascending=True)
        )
    ).rename(columns=glossary.DF_COLS_TO_NAME)


def best_weeks_song(data):
    """Best week song during the last weeks

    Args:
        data (pandas df): data

    Returns:
        pandas df: array for the best song during the last weeks
    """
    df = data[s.AnalysisScope.WEEKLY_BEST_SONGS.value].copy(deep=True)
    df[glossary.TIME_OF_DAY] = pd.to_datetime(df[glossary.TIME_OF_DAY])
    df.set_index(glossary.TIME_OF_DAY, inplace=True)
    weekly_top_songs = df.resample("W").apply(
        lambda x: x.loc[x[glossary.TIME_LISTENED].idxmax()]
    )
    # Select relevant columns for display
    weekly_top_songs = weekly_top_songs[
        [glossary.SONG, glossary.ARTIST, glossary.TIME_LISTENED]
    ]

    return weekly_top_songs


def most_skipped_songs(data, number_of_songs=10):
    """This function returns the most skipped songs.

    Args:
        data (pandas df): data
        number_of_songs (int, optional): number of songs you want to output.
                                        Defaults to 10.

    Returns:
        pandas df: array for the most skipped songs
    """
    data[glossary.SKIPPED] = data[glossary.REASON_END] == glossary.REASON_END_FWDBTN
    return (
        data[s.AnalysisScope.MOST_SKIPPED_SONGS.value]
        .groupby([glossary.SONG, glossary.ARTIST])
        .sum()
        .sort_values(glossary.SKIPPED, ascending=False)
        .head(number_of_songs)
        .reset_index()
        .rename(columns=glossary.DF_COLS_TO_NAME)
    )
