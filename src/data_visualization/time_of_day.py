""" 
This module contains functions to plot the time of day the user listened to music.
"""

import matplotlib.pyplot as plt

from factoring_tools import spotify_glossary as glossary

PLOT_FILENAME = "output/listening_time_bar_chart.png"


def plot_time_of_day(df):
    """This function plots the time of day the user listened to music.

    Args:
        df (pandas df): data
    """
    plt.figure(figsize=(10, 6))
    plt.bar(
        df.index, df[glossary.DF_COLS_TO_NAME[glossary.TIME_LISTENED]], color="skyblue"
    )
    plt.xlabel("Hour of the Day")
    plt.ylabel("Time Listened (hours)")
    plt.title("Listening Time by Hour of the Day")
    # display all the X-axis values, turn them horizontaly
    plt.xticks(df.index, rotation=45)

    # Save the plot as an image file
    plt.savefig(PLOT_FILENAME)
    plt.close()
