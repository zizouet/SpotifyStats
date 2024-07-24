from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Spacer, Image
import data_visualization.time_of_day as dv

import data_analysis as da
import factoring_tools.df_formatting as df_format

def generate_pdf(filename, most_listened_artist=None, most_listened_album=None, most_listened_song=None, listening_time=None, listening_time_of_day=None, skipped_songs = None):
    """ This function generates a pdf file with the data provided.

    Args:
        filename (String): path to save the file
        most_listened_artist (pandas df, optional): array of the most listened artists. Defaults to None.
        most_listened_album (pandas df, optional): array of the most listened albums. Defaults to None.
        most_listened_song (pandas df, optional): array of the most listened songs. Defaults to None.
        listening_time (Int, optional): Total Listening Time. Defaults to None.
        listening_time_of_day (pandas df, optional): array of the time of day the user listened to music. Defaults to None.
        skipped_songs (pandas df, optional): array of the most skipped songs. Defaults to None.

    Returns:
        String: filename
    """

    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []
    elements.append(Paragraph("Spotify Data Analysis", styles['Title']))

    elements.append(Spacer(1, 30)) 
    dv.plot_time_of_day(listening_time_of_day)
    

    #get the most listened artists from the parameters and display it
    ts = [('ALIGN', (1,1), (-1,-1), 'CENTER'),
     ('LINEABOVE', (0,0), (-1,0), 1, colors.black),
     ('LINEBELOW', (0,0), (-1,0), 1, colors.black),
     ('FONT', (0,0), (-1,0), 'Times-Bold'),
     ('LINEBELOW', (0,-1), (-1,-1), 1, colors.black),
     ('TEXTCOLOR',(0,0),(1,-1),colors.black)]
    
    if listening_time is not None:
        elements.append(Paragraph("Total Listening Time", styles['Heading1']))
        elements.append(Paragraph(f"{listening_time} hours", styles['Normal']))
        elements.append(Spacer(1, 25)) 
    
    heading_style = styles['Heading1']
    append_table(elements,"10 Most Listened Artists", most_listened_artist, heading_style,ts)
    append_table(elements,most_listened_album,"10 Most Listened Albums", heading_style,ts)
    append_table(elements,most_listened_song,"10 Most Listened Songs", heading_style,ts)
    append_table(elements,skipped_songs,"10 Most Skipped Songs", heading_style,ts)
    append_table(elements, "10 Most Listened Artists", most_listened_artist, heading_style,ts)

    img = Image(dv.plot_filename, width = 450, height = 300)
    elements.append(img)

    doc.build(elements)
    print(f"PDF file {filename} has been created.")
    return filename


def append_table(elements, title, data, title_style, table_style):
    """ This function appends a title and data to the elements list if the data is not None.

    Args:
        elements (list): element list to append to
        title (string): Title of the array you want to display
        data (pandas df): The array you want to display
        title_style (StyleSheet): style to apply to the title
        table_style (StyleSheet): style to apply to the table

    Returns:
        list: the elements list updated
    """
    if data is not None:
        elements.append(Paragraph(title, title_style))
        t = Table(df_format.df_to_list_of_list(data), style=table_style)
        elements.append(t)
        elements.append(Spacer(1, 25)) 
    return elements