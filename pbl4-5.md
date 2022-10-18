# PBL 4 & 5: Data preparation and understanding

## Problems

- [Preparation](#preparation)
- [Problem 1: Open a data set from .csv file in a pandas data frame](#problem-1-open-a-data-set-from-csv-file-in-a-pandas-data-frame)
- [Problem 2: Display some basic information about the data frame](#problem-2-display-some-basic-information-about-the-data-frame)
- [Problem 3: Delete any unnecessary columns](#problem-3-delete-any-unnecessary-columns)
- [Problem 4: Identify and address any missing values](#problem-4-identify-and-address-any-missing-values)
- [Problem 5: Find the unique values for categorical data](#problem-5-find-the-unique-values-for-categorical-data)
- [Problem 6: Merge the data with another data set to add the country codes](#problem-6-merge-the-data-with-another-data-set-to-add-the-country-codes)
- [Challenge](#challenge)
- [Problem 7: Basic stats](#problem-7-basic-stats)
- [Problem 8: Identify outliers](#problem-8-identify-outliers)
- [Problem 9: Explore how the numbers of male and female participants has changed over time](#problem-9-explore-how-the-numbers-of-male-and-female-participants-has-changed-over-time)
- [Problem 10: Splitting Winter and Summer data](#problem-10-splitting-winter-and-summer-data)
- [Problem 11: Exploring the relationship between m and f in winter and summer](#problem-11-exploring-the-relationship-between-m-and-f-in-winter-and-summer)
- [Further practice](#further-information-and-practice)


## Preparation

### Pre-requisite knowledge

It is assumed you attended the lectures that introduced pandas, dataframes and the dataframe methods used in this session.

### Set-up

For this session you will need a coding environment that has Python and the pandas library.

You can do this in a number of ways, e.g.

1. Create a new python project by creating a cloning the repository at <https://github.com/nicholsons/comp0035_pbl4.git>.

2. Create and activate a new virtual environment (or activate an existing environment)

3. Install pandas, matplotlib and openpyxl e.g. `pip install pandas openpyxl`)

### Data

The data in the activities is from the following sources.

- [London 2012 Ticket Sales](https://data.london.gov.uk/download/london-2012-ticket-sales/4711eb39-cb56-4f47-804d-e486dae89a1d/assembly-london-2012-ticket-sales.xls)
- [Paralympic medals and event info](https://www.paralympic.org/london-2012/results/medalstandings)
- [Logos](https://colorlib.com/wp/all-olympic-logos-1924-2022/)

The data is in the `paralympics_raw.csv` from the repository. The data has been modified such that it can be used for a
data cleaning activity.

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

We won't store the image information in the data set, but it would be useful to have fields in the data set that include
the year and the country code, so we can later more easily associate the data with the image files.

## Problem 1: Open a data set from .csv file in a pandas data frame

1. Create a new python code file (or open `pbl4_problem1.py`)
2. Add a line to `import pandas as pd`
3. Add a line of code to create a dataframe by reading the file from csv (see URL below if you don't have a dataset in
   your repo)
    - Use [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html). This method infers the
      column names from the first row by default. If you are using your own data set in .xlsx format then refer
      to [pandas.read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
    - If you didn't clone the classroom repo then you can still access the data file from GitHub using the URL
      `https://raw.githubusercontent.com/ucl-comp0035/comp0035_pbl4/master/data/paralympics_raw.csv?token=AHBUVRXLSGRV2Y2PEAXQXVTBPJFD2`

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
3. Decide what to do with the missing data (delete the row/column, or replace nulls with a computed or other value)
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

Both sets of data have a column with the country name, so you could merge the records based on those. The noc data has
more rows than the current dataframe, so you won't want to merge all rows from noc, only those that match existing rows
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
- Create a new dataframe that is a merge that returns all records from left (the paralympics data) and the matched
  records from the right (noc codes).
- This will only work for rows where the country name matches exactly, so you might want to check for NaNs again.
- Decide how to deal with the NaNs. This is a little more tricky as you need to replace a value in one column based on a
  condition in another. There will be more than one way to do this, I
  used [mask](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mask.html?highlight=mask#pandas.DataFrame.mask)
  .

## Challenge

The solution to this will be covered in the next PBL.

We still have a further step to carry out before we explore the data, however we will cover this in the next PBL. If you
want to try it yourself before then the issue is that the start and end date columns are text format and the date
doesn't include the year. Year is a separate field. You need to combine the dd-mmm and the yyyy to create a date for the
start and end columns. Once you have the two columns as dates, then add a new column called duration and calculate the
days between the start and end dates.

The functions you will need are covered in the 'How to ... data exploration' guide rather than the 'How to... data
preparation' guide. This was split for teaching activity convenience only, there is no clearly defined split between
preparation and exploration activities.

## Challenge solution

The start and end date columns are text format, and the date doesn't include the year. Year is a separate field. You
need to combine 'dd-mmm' and 'yyyy' to create a date for the start and end columns. Once you have the two columns as
dates, then add a new column called duration and calculate the days between the start and end dates.

The following solution is in `pbl4_challenge_solved.py`.

```python
# A possible solution to the challenge, please share if you have a neater or more efficient solution!

# Check the data type of the columns
print(df_prepared[['Year', 'Start', 'End']].dtypes)

# Check the format of the strings in Start and End by printing a couple of rows
print(df_prepared[['Year', 'Start', 'End']].head(2))

# Add the year to the Start and End columns. Year is int and Start/End are strings so to combine as strings you
# need to first convert the Year to string
# TODO: Consider if there is a case where the dates span year end e.g. December to January)
df_prepared["Start"] = + df_prepared["Start"] + '-' + df_prepared["Year"].astype(str)
df_prepared["End"] = + df_prepared["End"] + '-' + df_prepared["Year"].astype(str)
print(df_prepared[['Year', 'Start', 'End']].head(2))
print(df_prepared[['Year', 'Start', 'End']].dtypes)

# Change the column datatype to date-time format
# Pandas to_datetime handles most date formats so you can run the following without the format= and it will work
df_prepared['Start'] = pd.to_datetime(df_prepared['Start'], format='%d-%b-%Y')
df_prepared['End'] = pd.to_datetime(df_prepared['End'])
print(df_prepared[['Year', 'Start', 'End']].head(2))
print(df_prepared[['Year', 'Start', 'End']].dtypes)

# Create a duration column that calculates days between the start and end
df_prepared['Duration'] = df_prepared['End'] - df_prepared['Start']
print(df_prepared.head(5))
```

## Problem 7: Basic stats

[Pandas DataFrame.describe()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html?highlight=pandas%20dataframe%20describe#pandas.DataFrame.describe)
method provides some descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s
distribution, excluding NaN values.

The output varies depending on the data types however it returns stats such as the count, mean, std, min, first
quartile, median, third quartile, max on suitable columns.

Create a new Python code file and copy the code below. If you cloned the repository then you can edit `pbl5_problem1.py`
which already has the code in.

Add a line of code to print the stats generated by describe.

Note that when reading from csv there argument `parse_dates=['Start', 'End']` tells pandas to read the Start and End
columns as dates. We are also going to treat the Year column as a string rather than an integer otherwise it will be
included in the stats as if it were a number (`dtype={'Year': str`).

```python
import pandas as pd


def set_pandas_display_options(df):
    """ Sets the pandas display options based on the shape of the dataframe

    :param DataFrame df: the data
    """
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)


if __name__ == '__main__':
    df = pd.read_csv('data/paralympics_prepared.csv', parse_dates=['Start', 'End'], dtype={'Year': str})
    set_pandas_display_options(df)
    # Add your code here
```

For the coursework you should consider describing the data, however you do not need to analyse or interpret the
resulting stats since interpreting statistics is not part of this course.

## Problem 8: Identify outliers

Identifying outliers is subjective and techniques include:

- Plot the data (e.g., histogram, scatter plot, boxplot)
- Use common sense
- Use statistical tests

Since this course doesn't expect any knowledge or, nor teach any, statistics then we will check for outliers by creating
a chart, or plot, instead.

In this instance let’s create a boxplot. The boxplot will be created using pandas dataframe and displayed using the
matplotlib library.

Box plots have box from lower quartile to the upper quartile, with the median marked. 25% of the population is below
first quartile, 75% of the population is below third quartile.

![boxplot]({{ site.baseurl }}/assets/img/box_plot.png)

Source: [statinfer](https://statinfer.com/104-3-5-box-plots-and-outlier-dectection-using-python/)

They can help us to get an idea of the data distribution which in turn helps us to identify the outliers more easily.

If the box is pushed to one side, and some values are far away from the box, then it is an indication of outliers.

The following code shows a basic example of creating a boxplot with pandas and rendering the chart using matplotlib.
Numpy is only used to generate the random numbers.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])
bp = df.plot.box()
plt.show()
```

Add code to `pbl5_problem2.py` to generate a box plot for the paralympics data.

```python
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('data/paralympics_prepared.csv', parse_dates=['Start', 'End'], dtype={'Year': str})
    # Add code here to create the box plot
```

If you managed that, then you will have noticed that it plots all the variables on the same scale. Since the numbers are
significantly smaller for duration than the numbers for participants, the result is that we can't see the duration
boxplot clearly. To see each variable in its own subplot try adding the argument `subplots=True` in the `box()`
method.

If you want to save the generated plot to an image file (you might wish to for the coursework, though not essential)
try:

```python
df.plot.box().get_figure().savefig('{{ site.baseurl }}/assets/img/bp_example.png')
```

You should see an outlier in the duration. On examining the data you would find that this is because that yera the
Paralympics were in two locations, New York and Stoke Mandeville, and held on two different dates so the start and end
span both events. You could either choose to ignore the data, or you could perhaps try to find the data to allow you to
split this into two entries. We don't have the details currently to do the latter so if we created charts using the
duration field we may want to remove this outlier.

## Problem 9: Explore how the numbers of male and female participants has changed over time

Let's have a look at some of our data to start to understand it in more detail.

The 'how to...' guide suggested a histogram however our data doesn't really suit that since we aren't showing occurences
of different values, but a trend over a series of events.

The [DataFrame.plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html?highlight=plot#pandas.DataFrame.plot)
method provides a number of chart types as documented in the reference.

Create a [line plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.line.html) this time.

```python
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    cols = ["Participants (M)", "Participants (F)", "Participants"]
    df = pd.read_csv('data/paralympics_prepared.csv', usecols=cols)
    df.rename(columns={"Participants (M)": "Male", "Participants (F)": "Female", "Participants": "Total"}, inplace=True)
    # Your code goes here to create a line plot and show it

```

## Problem 10: Splitting Winter and Summer data

You will have noticed the line in the solution to problem 3 looks like a zigzag. We are plotting winter and summer
participants on the same axis and the numbers for winter are always lower.

1. Use the 'Type' column to identify rows to create one dataframe for summer events and one for winter events.

   The [pandas .loc function](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html?highlight=loc#pandas.DataFrame.loc)
   can be used.

   So `df2 = df.loc[df['ColName'] == 'Some text']` would create a new dataframe called df2 that has the data from
   dataframe df where the value in the column called 'ColName' is equal to the words 'Some text'.

2. Reset the index for each new dataframe. If you don't do this you will have row indices that are no longer sequential
   and this will cause an issue when you later try to label the axis. To reset
   try `df_summer.reset_index(drop=True, inplace=True)`

3. Create each line chart.

4. Show the charts i.e. `plt.show()`

Since we are just exploring the data we don't want to be too concerned with formating, however in this example it might
be worth formatting the x-axis to show every year that is in the data so that you can identify when the dip occurs. To
do that add the following code after _each chart_ but before `plt.show()`.

```python
# df in the code below should be the name of your summer or winter dataframe
# Add an extra parameter 'xticks=df.index' to df.plot.line(xticks=df.index) 
df.set_xticklabels(df['Year'])
plt.xticks(rotation=90)
```

So it looks like we would have data to answer the question "How has the number of male and female competitors in the
paralympics changed over time?".

## Problem 11: Exploring the relationship between m and f in winter and summer

It may be arguable whether this is beyond the exploration stage however let's have a go at seeing whether there is data
to support the second question.

Does the ratio of male:female competitors vary between winter and summer olympics?

Again we want the two dataframes for summer and winter data.

We could plot this as two ratios and generate a line charts e.g.

![Line chart showing m:f ratio]({{ site.baseurl }}/assets/img/ratio_line.png)

Try and explore the data using percentage stacked bar charts so you learn another chart style.

1. Sort the values by Type and Year The syntax
   is `df.sort_values(["ColName1", "ColName2"], ascending=(Fale, True), inplace=True)`
2. Add two new columns that each contain the result of calculating the % of male and female participants (e.g.
   Male/Total)
3. Create a new column that combines Type and Year to use as the x-axis
4. Create the stacked bar plot of the % for male and female
   Syntax `df.plot.bar(x='ColName1', y=['ColName2', 'ColName3'], stacked=True)`

## Further information and practice

- [How to create plots in pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html)

- Explore one of the other datasets in this repo e.g.
    - Prepare the `assembly-london-2012-ticket-sales.xlsx` data such that you could use it to later recreate the cycling
      chart shown on page 14 of the report
      titled [The Price of Gold: Lessons from the London 2012 ticket sales](https://www.london.gov.uk/sites/default/files/gla_migrate_files_destination/Economy%20Committee%20-%20The%20Price%20of%20Gold.pdf)
    - Prepare the `paralympic_medal_tables.xlsx` to show how a particular country's
      (pick any) medal performance has changed over the years.

- There is a nice example on Kaggle with a more extensive Olympic data
  set ([Exploring 120 years of Olympic history](https://www.kaggle.com/snocco/exploring-120-years-of-olympics-history/notebook))
  where the author, Stefano Nocco, walks through the preparation activities as well as exploring the data with various
  charts. If you want to access it you will need to create a Kaggle account so please be sure that you are happy with
  their terms and conditions before you proceed.
