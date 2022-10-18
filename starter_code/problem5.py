# Problem 5: Categorical data
import pandas as pd


# Set the pandas display options
def set_pandas_display_options(df):
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)


if __name__ == '__main__':
    df = pd.read_csv('data/paralympics_raw.csv')
    set_pandas_display_options(df)
    df.drop(['Events', 'Sports', 'Countries'], axis=1, inplace=True)
    df.dropna(axis=0, subset=['Participants (M)', 'Participants (F)'], inplace=True)
    df.fillna({'Type': 'Winter'}, inplace=True)

    # Find the unique values for the Type column

    # Remove the extra spaces from 'Summer   '. You can't use inplace=True as this is a Series action so you need to
    # replace the df["Type"] series with the result of the str.strip() function
