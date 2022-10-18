# Problem 2: Display some basic information about the data frame
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('data/paralympics_raw.csv')
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)

    # 1. Print the number of rows and columns in the DataFrame

    # 2. Print the first _n_ rows of data (e.g. 5)

    # 3. Print the column labels and data types. Note any columns that you don't think are needed.
