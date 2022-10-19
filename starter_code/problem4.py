# Problem 4: Identify and address any missing values
from pathlib import Path

import pandas as pd


def prepare_data():
    """
    Partially prepares the data by addressing:
        Problem 1: Read the csv into a DaraFrame and set the pandas display option to the number of rows and columns
        Problem 3: Remove the Events', 'Sports', 'Countries' columns
    :return: df: DataFrame with partially prepared data
    """
    paralympics_raw_csv = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    df = pd.read_csv(paralympics_raw_csv)
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)
    # Remove the Events', 'Sports', 'Countries' columns
    df.drop(['Events', 'Sports', 'Countries'], axis=1, inplace=True)
    return df


if __name__ == '__main__':
    # Code from problems 1 and 3:
    df_raw = prepare_data()

    # 1. Find and count the number of missing values e.g., Null `isnull().sum().sum()` or NaN `isna().sum().sum()`
    # and print the result

    # 2. Create a dataframe with the rows that contain missing values and print it

    # 3. Drop rows where there is a na in the Participants M or F columns

    # 4. Replace the NaN in Type column with 'Winter'
