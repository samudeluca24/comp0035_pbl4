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
    # Create a data frame with the NOC regions
    noc_csv = Path(__file__).parent.parent.joinpath('data', 'noc_regions.csv')
    df_noc = pd.read_csv(noc_csv)
    # Drop the 'notes' column
    df_noc.drop(['notes'], axis=1, inplace=True)
    # Merge the columns where df['Country'] matches df_noc['region']
    df_merged = df.merge(df_noc, how='left', left_on='Country', right_on='region')
    df_merged.drop(['region'], axis=1, inplace=True)
    # Manually add the 'NOC' code for Great Britain (GBR) and Republic of Korea (KOR)
    # This is a little more tricky as you need to replace a value in one column based on a condition in another
    # There will be more than one way to do this, I used a mask (condition).
    df_merged['NOC'].mask(df_merged['Country'] == 'Great Britain', 'GBR', inplace=True)
    df_merged['NOC'].mask(df_merged['Country'] == 'Republic of Korea', 'KOR', inplace=True)
    return df_merged


if __name__ == '__main__':
    df = prepare_data()

    # A possible solution to the challenge, please share if you have a neater or more efficient solution!

    # Check the data type of the columns
    print("\ndata type of the columns\n", df[['Year', 'Start', 'End']].dtypes)

    # Check the format of the strings in Start and End by printing a couple of rows
    print(df[['Year', 'Start', 'End']].head(2))

    # Add the year to the Start and End columns. Year is int and Start/End are strings so to combine as strings you
    # need to first convert the Year to string
    # TODO: Consider if there is a case where the dates span year end e.g. December to January)
    df["Start"] = df["Start"] + '-' + df["Year"].astype(str)
    df["End"] = df["End"] + '-' + df["Year"].astype(str)
    print(df[['Year', 'Start', 'End']].head(2))
    print(df[['Year', 'Start', 'End']].dtypes)

    # Change the column datatype to date-time format
    # Pandas to_datetime  handles most date formats so you can run the following without the format= and it will work
    # date time formats are here for reference https://docs.python.org/3/library/datetime.html
    df['Start'] = pd.to_datetime(df['Start'], format='%d-%b-%Y')
    df['End'] = pd.to_datetime(df['End'])
    print(df[['Year', 'Start', 'End']].head(2))
    print(df[['Year', 'Start', 'End']].dtypes)

    # Create a duration column that calculates days between the start and end
    df['Duration'] = df['End'] - df['Start']
    print(df.head(5))

    # The output of the above is in timedelta format, however we want to compare duration as int
    # Convert the format
    print(df['Duration'].dtypes)
    df['Duration'] = df['Duration'].dt.days.astype('int')
    print(df['Duration'].dtypes)

    # Save the prepared data to CSV
    prepared_csv_filepath = Path(__file__).parent.parent.joinpath('data', 'paralympics_prepared.csv')
    df.to_csv(prepared_csv_filepath, index=False)
