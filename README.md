# SpotifyStats



The goal of this application is to analyze your Spotify reports to understand who is your favorite artist, how much time do you listen each artists and other cool features.



Architecture of the project : 

The src file contains all the code necessary for the application to run.
The output contains all the data analysis which has been done by the application output under a PDF report.
The data folder contains some data to test.

The main routine takes care of the input data loading and calling the other routines.

The data displayed consist of : total listening time, top songs, artists, albums. Time of the day you're listening the most. Most Skipped songs and more to come.


How to handle the PyCache if you want to remove it : find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf