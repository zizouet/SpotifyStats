
import musicPlatform
import error 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt
import numpy as np
class Spotify(musicPlatform.Platform):

    def __init__(self):
            super().__init__(musicPlatform.PlatformSpecs.SPOTIFY)
            #care of special columns data for spotify
            self.useFullCols = ['ms_played',"master_metadata_album_artist_name",'master_metadata_track_name','ts']
            self.cols = ['ms_played','master_metadata_track_name',"master_metadata_album_album_name","master_metadata_album_artist_name",'ts',"conn_country","episode_name",'episode_show_name','offline_timestamp','incognito_mode','ip_addr_decrypted','offline','platform','reason_end','reason_start','shuffle','skipped','spotify_episode_uri','spotify_track_uri','user_agent_decrypted','username']
            self.trackName = "master_metadata_track_name"
            self.timePlayed = "ms_played"
            




           
    def topTracks(self):
        if self.isData == False :
             raise error.PreconditionNotMetError("need to load data in order before")
        
        timesColName = 'Times listened'
        hoursColName = 'Hours listened'
        self.topTracks = self.data.copy(deep=True)
        self.topTracks = self.topTracks[self.useFullCols]
        self.topTracks[timesColName] = self.topTracks.groupby(self.trackName)[self.trackName].transform('count')
        self.topTracks[hoursColName] = self.topTracks.groupby(self.trackName)[self.timePlayed].transform('sum')/1000/60/60
        self.topTracks = self.topTracks.drop_duplicates(self.trackName)
        self.topTracks = self.topTracks.drop(columns = ['ts',self.timePlayed])
        self.topTracks = self.topTracks[1:]
        self.topTracks.sort_values(hoursColName, inplace = True, ascending = False)

        self.topTracks.to_csv('sortbyTimeForEachTrack.csv')


    def listeningTimes(self):
        hours_listened_in_day = np.zeros(24)    
        total= 0
        for index, row in self.data.iterrows():
            time = int(row['ts'][11:13])
            timee = int(row['ms_played'])
            hours_listened_in_day[time]+= timee
            total+=timee
        heures = np.arange(24)
        hours_listened_in_day = hours_listened_in_day / 1000 /60 / 60

        plt.bar(heures, hours_listened_in_day)
        plt.xlabel('Heures de la journée')
        plt.ylabel("Nombre d'heures d'écoute")
        plt.title("Graphe des heures d'écoute en fonction des heures de la journée")
        plt.grid(True)
        plt.savefig("Horaire d'écoute")
        
        self.totalHours = total/1000 /60 / 60
    

    def makeClientID(self,identifier):
         self.clientID = identifier
    def makeClientSecret(self,secret):
         self.secret = secret
         
    def linkToPlaylistId(self,link):
         #create a substring from the link that starts at the starts occurence of a '/' and stops at the first occurence of a '?'
         start = link.rindex("/")+1
         end = link.rindex("?")
         playlistId = link[start:end:1]
         return playlistId

    def printPlaylist(self,link):
        

        client_credentials_manager = SpotifyClientCredentials(client_id=self.clientID, client_secret=self.secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        playlist_id = self.linkToPlaylistId(link)

        results = sp.playlist_tracks(playlist_id)
        tracks = results['items']

        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])

        for track in tracks:
            print(track['track']['name'])