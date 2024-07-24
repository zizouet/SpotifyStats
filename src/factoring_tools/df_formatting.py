

def df_to_list_of_list(df, index = True, header = True):
    """
    This function converts a pandas dataframe to a list of list.
    Index keeps the index of the dataframe
    Header keeps the header of the dataframe.
    """
    formatted = []
    if header:
        formatted.append(([df.index.name] if index else []) + [e for e in df.columns])
    for row in df.itertuples():
        formatted.append([e for e in row] if index else [e for e in row][1:])
    
    return formatted
    