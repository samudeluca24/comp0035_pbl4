# Problem 5: Categorical data
from pathlib import Path

import pandas as pd


def prepare_data():
    """
    Partially prepares the data by addressing:
        Problem 1: Read the csv into a DaraFrame and set the pandas display option to the number of rows and columns
        Problem 3: Remove the Events', 'Sports', 'Countries' columns
        Problem 4: Removes the rows with nulls in Participants columns; and replaces missing values in Type column
    :return: df: DataFrame with partially prepared data
    """
    # Problem 1. Load the data and set pandas display options to fit all rows and columns
    paralympics_raw_csv = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    df = pd.read_csv(paralympics_raw_csv)
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)
    # Problem 3. Remove the Events', 'Sports', 'Countries' columns
    df.drop(['Events', 'Sports', 'Countries'], axis=1, inplace=True)
    # Problem 4. Removes the rows with nulls in Participants columns; and replaces missing values in Type column.
    df.dropna(axis=0, subset=['Participants (M)', 'Participants (F)'], inplace=True)
    df.fillna({'Type': 'Winter'}, inplace=True)
    return df


if __name__ == '__main__':
    # Code from problems 1-4
    df_raw = prepare_data()

    # Find the unique values for the Type column

    # Remove the extra spaces from 'Summer   '. You can't use inplace=True as this is a Series action so you need to
    # replace the df["Type"] series with the result of the str.strip() function
