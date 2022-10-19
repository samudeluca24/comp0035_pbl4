# Problem 6: Joining data sets
from pathlib import Path

import pandas as pd


def prepare_data():
    """
        Partially prepares the data by addressing:
            Problem 1: Reads the csv into a DataFrame and sets pandas display options to the number of rows and columns
            Problem 3: Removes the Events', 'Sports', 'Countries' columns
            Problem 4: Removes the rows with nulls in Participants columns; and replaces missing values in Type column
            Problem 5: Removes the trailing spaces from the text entries in the Type column
        :return: df: DataFrame with partially prepared data
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
    return df


if __name__ == '__main__':
    # Code from problems 1 to 5:
    df_raw = prepare_data()

    # Create a data frame with the NOC regions

    # Drop the 'notes' column

    # Merge the columns where df['Country'] matches df_noc['region']

    # Manually add the 'NOC' code for Great Britain (GBR) and Republic of Korea (KOR)
    # This is a little more tricky as you need to replace a value in one column based on a condition in another
    # There will be more than one way to do this, I used a mask (condition).
