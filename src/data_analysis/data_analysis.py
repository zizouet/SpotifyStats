
import pandas as pd
import data_analysis.analysis_scope as s 
import factoring_tools.spotify_glossary as glossary
import factoring_tools.time_formatting as format
import report_generation.pdf_generation as pdf



def full_analysis(data, number_of_items = 10):
    """
    This function is a polymorphic function that returns the most listened artist, album, or song.
    """
    top_artist = most_listened_artist(data, number_of_items).rename(columns={glossary.time_listened:"Time Listened (in hours)"})
    top_album = most_listened_album(data, number_of_items)
    top_song = most_listened_song(data, number_of_items).rename(columns={glossary.time_listened:"Time Listened (in hours)"})
    top_skipped_songs = most_skipped_songs(data)
    


    pdf.generate_pdf("output/SpotifyDataAnalysis.pdf", most_listened_artist=top_artist, most_listened_album=top_album, most_listened_song=top_song, listening_time=listening_time(data), listening_time_of_day=listening_time_of_day(data),skipped_songs=top_skipped_songs)
    
    
    
def __most_listened(data, columns, item_analyzed, number_of_items=1):
    """
    This function is a polymorphic function that returns the most listened artist, album, or song.
    """
    return round(format.ms_to_hours(data[columns].groupby(item_analyzed).sum().sort_values(glossary.time_listened, ascending=False).head(number_of_items))).reset_index().rename(columns = glossary.df_cols_to_name)

def most_listened_artist(data, number_of_artists=1):
    return __most_listened(data, s.AnalysisScope.MOST_LISTENED_ARTIST.value, glossary.artist, number_of_artists)

def most_listened_album(data, number_of_albums=1):
    return __most_listened(data, s.AnalysisScope.MOST_LISTENED_ALBUM.value, [glossary.album, glossary.artist], number_of_albums)
    

def most_listened_song(data, number_of_songs=1):
    return __most_listened(data, s.AnalysisScope.MOST_LISTENED_SONG.value, [glossary.song,glossary.artist], number_of_songs)
    


def listening_time(data):
    """
    This function returns the total time listened to music.
    """
    return round(format.ms_to_hours(data[glossary.time_listened].sum()))

def listening_time_of_day(data):
    """
    This function returns the listening time during each hour of the day.
    E.g. : It allows you to see if you listen music more at night or during the day.
    """
    hours = data[glossary.time_of_day].apply(format.extract_hour_from_timestamp)
    return round(format.ms_to_hours(data[s.AnalysisScope.LISTENING_TIME_OF_DAY.value].assign(hour=hours).groupby('hour').sum().sort_values('hour', ascending=True))).rename(columns= glossary.df_cols_to_name)

def best_songs_through_time(data):
    """
    Best week song during the last weeks 
    """
    df = data[s.AnalysisScope.WEEKLY_BEST_SONGS.value].copy(deep=True)
    df[glossary.time_of_day] = pd.to_datetime(df[glossary.time_of_day])
    df.set_index(glossary.time_of_day,inplace=True)
    weekly_top_songs = df.resample('W').apply(lambda x: x.loc[x[glossary.time_listened].idxmax()])
    # Select relevant columns for display
    weekly_top_songs = weekly_top_songs[['master_metadata_track_name', 'master_metadata_album_artist_name', 'ms_played']]

    return weekly_top_songs


def most_skipped_songs(data, number_of_songs = 10):
    data[glossary.skipped] = data[glossary.reason_end] == glossary.reason_end_fwdbtn
    return data[s.AnalysisScope.MOST_SKIPPED_SONGS.value].groupby([glossary.song, glossary.artist]).sum().sort_values(glossary.skipped, ascending=False).head(number_of_songs).reset_index().rename(columns=glossary.df_cols_to_name)



