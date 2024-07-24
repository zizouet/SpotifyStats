""" Main module to run the program. """

from data_analysis import data_analysis as da
from input_handling import loading_input as li


def main():
    """
    main function to run the program.
    """
    # load data
    df = li.loading_data_from("data/MesDatas")
    # check if data is loaded
    if df is None:
        print("No data to analyze")
        return
    # call routine to analyze the data
    da.full_analysis(df)


if __name__ == "__main__":
    main()
