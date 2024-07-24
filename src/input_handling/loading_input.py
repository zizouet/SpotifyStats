import glob
import os

import pandas as pd

import factoring_tools.spotify_glossary as glossary


def loading_data_from(folder_path):
    """This function loads the data from the data folder.

    Args:
        folder_path (String): folder/file path to the data

    Returns:
        pandas df: the dataframe from the JSON data
    """
    # Load all the json from a directory
    try:
        json_files = glob.glob(os.path.join(folder_path, "*.json"))
    except Exception as e:
        print(f"Error reading the directory: {e}")
        return None

    dfs = []
    for file in json_files:
        try:
            df = pd.read_json(file)
            for col in df:
                # Check JSON have a good format else skip the file
                if col not in glossary.df_cols:
                    print(f"Wrong JSON format in {file}")
                    print(f"Column {col} not in glossary.df_cols")
                    continue
            dfs.append(df)
        except ValueError as e:
            print(f"Error reading {file}: {e}")
            return None
    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
    else:
        print("No valid JSON files were found.")
        return None

    return combined_df
