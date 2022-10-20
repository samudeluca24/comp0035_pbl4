from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


if __name__ == '__main__':
    prepared_csv_filepath = Path(__file__).parent.parent.joinpath('data', 'paralympics_prepared.csv')
    # You only need the participants columns so only read these into the dataframe
    cols = ["Participants (M)", "Participants (F)", "Participants"]
    df = pd.read_csv(prepared_csv_filepath, usecols=cols)
    # Change the column names (shorter)
    df = df.rename(columns={"Participants (M)": "Male", "Participants (F)": "Female", "Participants": "Total"})

    # Add code here to create and show the line plot
