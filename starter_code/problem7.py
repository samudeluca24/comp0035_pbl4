'''
Problem 7 Challenge

The start and end date columns are text format and the date doesn't include the year.
Year is a separate field.
You need to combine the dd-mmm and the yyyy to create a date for the start and end columns.
Once you have the two columns as dates, then add a new column called duration and calculate the
days between the start and end dates.

The functions you will need are covered in the 'How to ... data
exploration' guide rather than the 'How to... data preparation' guide.
'''
from pathlib import Path

import pandas as pd


def prepare_data():
    """
        Prepares the data and saves to file by addressing:
            Problem 1: Reads the csv into a DataFrame and sets pandas display options to the number of rows and columns
            Problem 3: Removes the Events', 'Sports', 'Countries' columns
            Problem 4: Removes the rows with nulls in Participants columns; and replaces missing values in Type column
            Problem 5: Removes the trailing spaces from the text entries in the Type column
            Problem 6: Merges the NOC code column from the noc_csv and adds missing values
        :return: None
    """
    # Problem 1. Load the data and set pandas display options to fit all rows and columns
    paralympics_raw_csv = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    df = pd.read_csv(paralympics_raw_csv)
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)
    # Problem 3. Remove the Events', 'Sports', 'Countries' columns
    df.drop(['Events', 'Sports', 'Countries'], axis=1, inplace=True)
    # Problem 4: Removes the rows with nulls in Participants columns; and replaces missing values in Type column.
    df.dropna(axis=0, subset=['Participants (M)', 'Participants (F)'], inplace=True)
    df.fillna({'Type': 'Winter'}, inplace=True)
    # Problem 5: Removes the trailing spaces from the text entries in the Type column
    df['Type'] = df['Type'].str.strip()
    # Problem 6: Merge the NOC code column from the noc_csv
    # Open the noc_regions.csv in a dataframe
    noc_csv = Path(__file__).parent.parent.joinpath('data', 'noc_regions.csv')
    df_noc = pd.read_csv(noc_csv)
    # Drop the 'notes' column
    df_noc = df_noc.drop(['notes'], axis=1)
    # Merge the columns where df['Country'] matches df_noc['region']
    df_merged = df.merge(df_noc, how='left', left_on='Country', right_on='region')
    df_merged = df_merged.drop(['region'], axis=1)
    # Manually add the 'NOC' code for Great Britain (GBR) and Republic of Korea (KOR)
    # You need to replace a value in one column based on a condition in another.
    # There will be more than one way to do this, the following uses a mask (condition).
    df_merged = df_merged['NOC'].mask(df_merged['Country'] == 'Great Britain', 'GBR')
    df_merged = df_merged['NOC'].mask(df_merged['Country'] == 'Republic of Korea', 'KOR')
    return df_merged


if __name__ == '__main__':
    df_raw = prepare_data()

    # Check the data type of the columns

    # Check the format of the strings in Start and End by printing a couple of rows

    # Add the year to the Start and End columns. Year is int and Start/End are strings so to combine as strings you
    # need to first convert the Year to string

    # Change the Start/End columns datatype to datetime format
    # Pandas to_datetime handles most date formats so you can use it without the format= and it will work

    # Create a duration column that calculates days between the start and end

    # The output of the above is in timedelta format, however we want to compare duration as int
    # Convert the format from datetime to int



