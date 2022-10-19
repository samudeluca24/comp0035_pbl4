from pathlib import Path

import pandas as pd


if __name__ == '__main__':
    prepared_csv_filepath = Path(__file__).parent.parent.joinpath('data', 'paralympics_prepared.csv')
    df_prepared = pd.read_csv(prepared_csv_filepath)

    # Add code here to print the stats returned by describe
