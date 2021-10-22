# Problem 3: Delete any unnecessary columns
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('data/paralympics_raw.csv')
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)
    print(df.info())

    # 1. Drop the list of named columns `['Events', 'Sports', 'Countries']

    # 2. Print the column labels and data types again, or check the shape which should be lower than the original
    # column count
