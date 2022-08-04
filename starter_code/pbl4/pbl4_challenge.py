'''
Challenge

The start and end date columns are text format and the date doesn't include the year.
Year is a separate field.
You need to combine the dd-mmm and the yyyy to create a date for the start and end columns.
Once you have the two columns as dates, then add a new column called duration and calculate the
days between the start and end dates.

The functions you will need are covered in the 'How to ... data
exploration' guide rather than the 'How to... data preparation' guide.
'''

import pandas as pd


def set_pandas_display_options(df):
    """ Sets the pandas display options based on the shape of the dataframe

    :param DataFrame df: the data
    """
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)


def prepare_data(df):
    """
    Prepares the paralympics data using the steps covered in problems 1 to 6

    :param DataFrame df: the raw data
    :return: the prepared paralympic data
    :rtype: DataFrame
    """
    df.drop(['Events', 'Sports', 'Countries'], axis=1, inplace=True)
    df.dropna(axis=0, subset=['Participants (M)', 'Participants (F)'], inplace=True)
    df.fillna({'Type': 'Winter'}, inplace=True)
    df['Type'] = df['Type'].str.strip()
    df_noc = pd.read_csv('data/noc_regions.csv')
    df_noc.drop(['notes'], axis=1, inplace=True)
    df_merged = df.merge(df_noc, how='left', left_on='Country', right_on='region')
    df_merged.drop(['region'], axis=1, inplace=True)
    df_merged['NOC'].mask(df_merged['Country'] == 'Great Britain', 'GBR', inplace=True)
    df_merged['NOC'].mask(df_merged['Country'] == 'Republic of Korea', 'KOR', inplace=True)
    return df_merged


if __name__ == '__main__':
    df_raw = pd.read_csv('data/paralympics_raw.csv')
    df = prepare_data(df_raw)
    set_pandas_display_options(df)

    # Check the data type of the columns

    # Check the format of the strings in Start and End by printing a couple of rows

    # Add the year to the Start and End columns. Year is int and Start/End are strings so to combine as strings you
    # need to first convert the Year to string

    # Change the Start/End columns datatype to datetime format
    # Pandas to_datetime handles most date formats so you can use it without the format= and it will work

    # Create a duration column that calculates days between the start and end

    # The output of the above is in timedelta format, however we want to compare duration as int
    # Convert the format from datetime to int
