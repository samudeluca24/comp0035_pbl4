# Problem 3: Delete any unnecessary columns
from pathlib import Path

import pandas as pd


def prepare_data():
    """
    Provides a solution to problem 1.
    :return: df: DataFrame with the raw data
    """
    paralympics_raw_csv = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    df = pd.read_csv(paralympics_raw_csv)
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)
    return df


if __name__ == '__main__':
    # Code from problems 1:
    df_raw = prepare_data()

    print(df_raw.columns)

    # 1. Drop the list of named columns `['Events', 'Sports', 'Countries']

    # 2. Print the column labels again, or check the shape which should be lower than the original column count
