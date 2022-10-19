# Problem 2: Display some basic information about the data frame
from pathlib import Path

import pandas as pd


def prepare_data():
    """
    Provides a solution to problem 1.
    :return:
    """
    paralympics_raw_csv = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    df = pd.read_csv(paralympics_raw_csv)
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)
    return df


if __name__ == '__main__':
    # Code from problem 1:
    df_raw = prepare_data()

    # 1. Print the number of rows and columns in the DataFrame

    # 2. Print the first _n_ rows of data (e.g. 5)

    # 3. Print the column labels. Note any columns that you don't think are needed.

    # 4. Print the column labels and data types.
