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
            Problem 7: Add a duration column that calculates the difference between the start and end dates
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
    # Problem 7: Add a column to calculate duration
    # Replace the start and end columns by combining the Start & Year, and End & Year columns
    df_merged["Start"] = df_merged["Start"] + '-' + df_merged["Year"].astype(str)
    df_merged["End"] = df_merged["End"] + '-' + df_merged["Year"].astype(str)
    # Change the column datatype to date-time format
    # Pandas to_datetime  handles most date formats so you can run the following without the format= and it will work
    # date time formats are here for reference https://docs.python.org/3/library/datetime.html
    df_merged['Start'] = pd.to_datetime(df_merged['Start'], format='%d-%b-%Y')
    df_merged['End'] = pd.to_datetime(df_merged['End'])
    # Create a duration column that calculates days between the start and end
    df_merged['Duration'] = df_merged['End'] - df_merged['Start']
    # The output of the above is in timedelta format, however we want to compare duration as int
    # Convert the format
    df_merged['Duration'] = df_merged['Duration'].dt.days.astype('int')
    # Save the file
    prepared_csv_filepath = Path(__file__).parent.parent.joinpath('data', 'paralympics_prepared.csv')
    df_merged.to_csv(prepared_csv_filepath, index=False)


if __name__ == '__main__':
    prepare_data()
    prepared_csv_filepath = Path(__file__).parent.parent.joinpath('data', 'paralympics_prepared.csv')
    df_prepared = pd.read_csv(prepared_csv_filepath)

    # Add code here to print the stats returned by describe
