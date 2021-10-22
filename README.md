# COMP0035 PBL 4: Data preparation

## Preparation

### Pre-requisite knowledge

It is assumed you have already completed the "How to prepare a data set using pandas" activity in week 3 on Moodle. That
activity introduces pandas, dataframes and the dataframe methods used in this session.

The [pandas cheat sheet](pandas_cheat_sheet.md) in this repository lists methods from the 'how to..' guides that would
be useful for this PBL session.

### Set-up

For this session you will need a coding environment that has Python and the pandas library.

You can do this in a number of ways e.g.

- Use an existing python project (e.g. PBL1) and install pandas (e.g. `pip install pandas`)
- Use a Jupyter notebook. For Jupyter ignore the `print` commands as you don't need those in Jupyter e.g. the code would
  be `df.shape` and not `print(df.shape)`.
- Create a new python project by creating a copy of the GitHub classroom assignment] as follows:

1. Accept the [GitHub classroom assignment](https://classroom.github.com/a/0BkaE0Hn) to create a new repo
2. Copy the URL of the newly created repo
3. Create a project in your Python coding environment (e.g. PyCharm, VS Code, Atom, PythonAnywhere etc) by cloning from
   the URL
4. Create a venv (PBL1 explained how to create a venv)
5. Install pandas (PBL 1 explained how to add packages to a venv e.g. `pip install pandas`)

### Data

The data in the activities is from the following sources.

- [London 2012 Ticket Sales](https://data.london.gov.uk/download/london-2012-ticket-sales/4711eb39-cb56-4f47-804d-e486dae89a1d/assembly-london-2012-ticket-sales.xls)
- [Paralympic medals and event info](https://www.paralympic.org/london-2012/results/medalstandings)
- [Logos](https://colorlib.com/wp/all-olympic-logos-1924-2022/)

The data has been modified such that it can be used for a data cleaning activity.

You can either use your own dataset for this or [paralympics_raw.csv](data/paralympics_raw.csv) from the directory. If
using your own then place a copy in the `/data` directory of the project.

### Questions to be answered (paralympics data set)

To guide the data preparation activity, assume that the questions to answer from the data set are:

- How has the number of male and female competitors in the paralympics changed over time?
- Does the ratio of male:female competitors vary between winter and summer olympics?

In addition to the charts that will attempt to answer the questions, the web app will also feature a searchable history
of paralympic events with information about each event. The event information will include the country flag, the
paralympic logo, start and end dates and the duration of the event.

To answer the questions requires the following data fields:

- Year
- Summer / Winter
- Number male competitors
- Number female competitors

To generate the event pages requires:

- Logo (these are stored in a naming convention YYYY_HOST CITY NAME)
- Flag (these are stored with a naming convention that uses the NOC three letter region codes)
- Event start and end dates
- Event duration

We won't store the image information in the data set but it would be useful to have fields in the data set that include
the year and the country code so we can later more easily associate the data with the image files.

## Problem 1: Open a data set from .csv file in a pandas data frame

1. Create a new python code file (or open `pbl4_problem1.py`)
2. Add a line to import pandas as pd
3. Add a line of code to create a dataframe by reading the file from csv (see URL below if you don't have a dataset in
   your repo)
    - Use [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html). This method infers the
      column names from the first row by default. If you are using your own data set in .xlsx format then refer
      to [pandas.read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
    - If you didn't clone the classroom repo then you can still access the data file from GitHub using the URL
      `https://raw.githubusercontent.com/nicholsons/comp0035_pbl4/master/data/paralympics_raw.csv?token=AHBUVRXMMNPI7VSWY4P34IDBO2TES`

4. Print the dataframe
    - If you are using the PBL dataset you might find it useful to set dataframe options to display the all columns and
      rows for using

        ```python
        pd.set_option('display.max_rows', df.shape[0] + 1)
        pd.set_option('display.max_columns', df.shape[1] + 1)
        ```

## Problem 2: Display some basic information about the data frame

1. Print the number of rows and columns in the DataFrame
2. Print the first _n_ rows of data (e.g. 5)
3. Print the column labels and data types. Note any columns that you don't think are needed.

## Problem 3: Delete any unnecessary columns

Given the summary of the visualisations and web app in the introduction it seems you could delete the columns for
Events, Sports and Countries.

1. Drop the list of named columns `['Events', 'Sports', 'Countries']`
2. Print the column labels and data types again, or check the shape which should be lower than the original column count

Hint: `inplace=True` replaces the current dataframe contents.

## Problem 4: Identify and address any missing values

1. Find and count the number of missing values e.g., Null `isnull().sum().sum()` or NaN `isna().sum().sum()`
2. Create a dataframe with the rows that contain missing values `missing_rows = df[df.isna().any(axis=1)]` and print it
3. Decide what to do with the missing data (delete the row/columm, or replace nulls with a computed or other value)
    - If using the paralympics data you might decide to drop the row that doesn't have info on the male and female
      participants as it would be incorrect to guess or compute this, however the missing 'Type' data could be inferred
      from the dates since the years correspond to 'Winter' events.
    - Drop the row with missing Participants (M) and Participants (F) using `dropna()`
    - For the Type column, fill the NaNs with 'Winter' using `fillna()`

The syntax
for [dropna](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html?highlight=dropna#pandas.DataFrame.dropna)
is:

```python
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
```

Where rows are `axis=0` and columns are `axis=1`.

To remove only rows with null/Nan in the Participants (M) and Participants (F) the first row then you could drop a row
rather than a column by specifying to only drop rows where the missing values are in particular columns:

```python
df.dropna(axis=0, subset=['AColName', 'AnotherColName'], inplace=True)
```

## Problem 5: Find the unique values for categorical data

Checking the unique values for categorical data could help to identify if there are any inconsistent entries. The only
categorical column that we have is Type so try to identify the unique values for this column.

Use `df['ColName'].unique()`.

Deal with any inconsistent values.

## Problem 6: Merge the data with another data set to add the country codes

The flag images are referenced by the NOC region code. Let's assume that we need to add the NOC region code to each of
our rows in the data frame.

The NOC region codes are in a csv file: `/data/noc_regions.csv`.

Both sets of data have a column with the country name so you could merge the records based on those. The noc data has
more rows than the current dataframe so you won't want to merge all rows from noc, only those that match existing rows
in the dataframe.

If you have 2 dataframes with common indices then you could use join.
[join two dataframes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html?highlight=join#pandas.DataFrame.join):

In this case we are merging on non-key columns so will
use [merge](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html?highlight=merge#pandas.DataFrame.merge)
.

```python
DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False,
                sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
```

To merge data you need to have a basic understanding of join types which is specified by the `how=` argument.

- `how='left'` Returns all records from the left data frame, and the matched records from the right dataframe
- `how='right'` Returns all records from the right dataframe, and the matched records from the left dataframe
- `how='outer'` Returns all records when there is a match in either left or right dataframe. (Union)
- `how='inner'` Returns records that have matching values in both dataframes. (Intersection)

Try to solve the problem:

- Create a new dataframe with noc codes, this will be the 'right' dataframe.
- Explore the noc dataframe to determine which column has the country name
- Drop any unnecessary columns from the noc codes dataframe.
- Create a new dataframe that is a merge that returns all records from left (the paralypmpics data) and the matched
  records from the right (noc codes).
- This will only work for rows where the country name matches exactly so you might want to check for NaNs again.
- Decide how to deal with the NaNs. This is a little more tricky as you need to replace a value in one column based on a
  condition in another. There will be more than one way to do this, I
  used [mask](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mask.html?highlight=mask#pandas.DataFrame.mask)
  .

## Challenge

The solution to this will be covered in the next PBL.

We still have a further step to carry out before we explore the data, however we will cover this in the next PBL. If you
want to try it yourself before then the issue is that the start and end date columns are text format and the date
doesn't include the year. Year is a separate field. You need to combine the dd-mmm and the yyyy to create a date for the
start and end columns. Once you have the two columns as dates, then add a new column called duration and calulate the
days between the start and end dates.

The functions you will need are covered in the 'How to ... data exploration' guide rather than the 'How to... data
preparation' guide. This was split for teaching activity convenience only, there is no clearly defined split between
preparation and exploration activities.

## Further practice

There are other data sets in the repository that you could try to prepare for a specific purpose e.g.

1. Prepare the [assembly-london-2012-ticket-sales.xlsx](data/assembly-london-2012-ticket-sales.xls) data such that you
   could use it to later recreate the cycling chart shown on page 14 of the report
   titled [The Price of Gold: Lessons from the London 2012 ticket sales](https://www.london.gov.uk/sites/default/files/gla_migrate_files_destination/Economy%20Committee%20-%20The%20Price%20of%20Gold.pdf)
2. Prepare the [paralympic medal tables data set](data/paralympic_medal_tables.xlsx) to show how a particular country's
   (pick any) medal performance has changed over the years.

There is a nice example on Kaggle with a more extensive Olympics data
set ([Exploring 120 years of Olympic history](https://www.kaggle.com/snocco/exploring-120-years-of-olympics-history/notebook))
where the author, Stefano Nocco, walks through the preparation activities. If you want to access it you will need to
create a Kaggle account so please be sure that you are happy with their terms and conditions before you proceed. 