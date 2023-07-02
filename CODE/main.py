import json
import findspark
import pandas as pd
import numpy as np
import spotify as sp
import musicPlatform
from enum import Enum

# name of all parsed data 



SPOTIFYSHORT = ["msPlayed","artistName","trackName","endTime"]
YTMUSIC = ['titleUrl', 'title','time','header','products','subtitles','activityControls']


#choose path to your file
files = ['DATA/Lina/0.json','DATA/Lina/1.json','DATA/Lina/2.json','DATA/Lina/3.json']

def main ():
    print("Running...")
    a = sp.Spotify()
    a.loadFiles(files)
    a.makeClientSecret('cb6c92e52b564d6aa581b29d56aa73c3')
    a.makeClientID('86cccd710bef4f53aaeca120fcbcf2f1')
    a.listeningTimes()
    a.topTracks()
    #linkeee = input("Entrez l'URL d'une playlist Spotify : ")
    #a.printPlaylist( linkeee )
    
main()
    








