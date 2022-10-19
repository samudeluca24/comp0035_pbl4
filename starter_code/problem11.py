from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


if __name__ == '__main__':
    prepared_csv_filepath = Path(__file__).parent.parent.joinpath('data', 'paralympics_prepared.csv')
    df = pd.read_csv(prepared_csv_filepath, parse_dates=['Start', 'End'], dtype={'Year': str, 'Type': str})
    df = df.rename(columns={"Participants (M)": "Male", "Participants (F)": "Female", "Participants": "Total"})
    cols = ["Male", "Female", "Total"]

    # 1. Create two new dataframes, one with winter data and one with summer data using .loc
    # Syntax will be `df.loc[df['Column'] condition]`. You can use conditions such as == (equals)

    # 2. Reset the index of each of the new dataframes e.g. df_summer.reset_index(drop=True, inplace=True)

    # 3. Create two line plots, for each x will be 'Year' and y will be the variable 'cols' (see line 8)

    # 4. Show the plots

