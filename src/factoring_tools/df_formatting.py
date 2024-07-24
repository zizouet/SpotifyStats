def df_to_list_of_list(df, index=True, header=True):
    """This function converts a pandas dataframe to a list of list.
    Index keeps the index of the dataframe
    Header keeps the header of the dataframe.

    Args:
        df (pandas df): data
        index (bool, optional): if you want to keep the index column. Defaults to True.
        header (bool, optional): if you want to keep the header row. Defaults to True.

    Returns:
        Python List[]: the array for the dataframe.
    """
    formatted = []
    if header:
        formatted.append(([df.index.name] if index else []) + [e for e in df.columns])
    for row in df.itertuples():
        formatted.append([e for e in row] if index else [e for e in row][1:])

    return formatted
