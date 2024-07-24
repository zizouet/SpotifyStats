
import data_analysis.data_analysis as data_analysis
import input_handling.loading_input as loading_input

def main():
    """
    main function to run the program.
    """
    #load data
    df = loading_input.loading_data_from('data/Lina')
    #check if data is loaded
    if df is None:
        print("No data to analyze")
        return
    #call routine to analyze the data
    data_analysis.full_analysis(df)



if __name__ == "__main__":
    main()


    