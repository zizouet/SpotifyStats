import json
import findspark
import pandas as pd
import numpy as np
from enum import Enum

# name of all parsed data 

#Spotify full time data
SPOTIFYFULL = ['ms_played','master_metadata_track_name','master_metadata_track_name','ts',"conn_country","episode_name",'episode_show_name','offline_timestamp','incognito_mode','ip_addr_decrypted','offline','platform','reason_end','reason_start','shuffle','skipped','spotify_episode_uri','spotify_track_uri','user_agent_decrypted','username']
#Spotify short time data approximately a year
SPOTIFYSHORT = ["msPlayed","artistName","trackName","endTime"]
YTMUSIC = ['titleUrl', 'title','time','header','products','subtitles','activityControls']


#choose path to your file
files = ['Lina/0.json','Lina/1.json','Lina/2.json','Lina/3.json']

def main (args):
    findspark.init()
    import pyspark # only run after findspark.init()
    from pyspark.sql import SparkSession

    








