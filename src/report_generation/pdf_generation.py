from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, Image
import data_visualization.time_of_day as dv

import data_analysis as da
import factoring_tools.df_formatting as df_format

def generate_pdf(filename, most_listened_artist=None, most_listened_album=None, most_listened_song=None, listening_time=None, listening_time_of_day=None, skipped_songs = None):
    """
    This function generates a pdf file with the data provided.
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
    
    if most_listened_artist is not None:
        elements.append(Paragraph("10 Most Listened Artists", styles['Heading1']))
        t = Table(df_format.df_to_list_of_list(most_listened_artist), style=ts)
        elements.append(t)
        elements.append(Spacer(1, 25)) 
    if most_listened_album is not None:
        elements.append(Paragraph("10 Most Listened Albums", styles['Heading1']))
        a = df_format.df_to_list_of_list(most_listened_album)
        t = Table(df_format.df_to_list_of_list(most_listened_album), style=ts)
        elements.append(t)
        elements.append(Spacer(1, 45)) 
    
    if most_listened_song is not None:
        elements.append(Paragraph("10 Most Listened Songs", styles['Heading1']))
        t = Table(df_format.df_to_list_of_list(most_listened_song), style=ts)
        elements.append(t)
        elements.append(Spacer(1, 25)) 
    if skipped_songs is not None:
        elements.append(Paragraph("10 Most Skipped Songs", styles['Heading1']))
        t = Table(df_format.df_to_list_of_list(skipped_songs), style=ts)
        elements.append(t)
        elements.append(Spacer(1, 25)) 

    img = Image(dv.plot_filename, width = 450, height = 300)
    elements.append(img)

    
    



    doc.build(elements)
    print(f"PDF file {filename} has been created.")
    return filename