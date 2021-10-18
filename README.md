# COMP0035 Problem based learning session 4: Data preparation

## Preparation
### Pre-requisite knowledge

It is assumed you have already completed the **How to prepare a data set using pandas** activity in week 4. That
activity introduces pandas, dataframes and the dataframe methods used in this session.

The [pandas cheat sheet](pandas_cheat_sheet.md) in this repository lists the methods used in the 'how to' guide.

### Set-up

This session you will be coding. You will need a coding environment that has Python and the pandas library.

You can either use and existing python project, install pandas (e.g. `pip install pandas`) and access the data file from GitHub using the URL 

1. Accept the GitHub classroom assignment to create a new repo, copy the URL of the newly created repo 
2. Create a project in your Python coding environment (e.g. PyCharm, VS Code, Atom, PythonAnywhere etc) by cloning from the URL
3. Create a venv (PBL1 explained how to create a venv)
4. Install pandas (PBL 1 explained how to add packages to a venv e.g. pip install pandas)

You can either use your own dataset for this or the paralympics_raw.csv from the directory.

### Data
The data in the activities is from the following sources.

- [London 2012 Ticket Sales](https://data.london.gov.uk/download/london-2012-ticket-sales/4711eb39-cb56-4f47-804d-e486dae89a1d/assembly-london-2012-ticket-sales.xls)
- [Paralympic medals and event info](https://www.paralympic.org/london-2012/results/medalstandings)
- [Logos](https://colorlib.com/wp/all-olympic-logos-1924-2022/)

The data has been modified such that it can be used for a data cleaning activity.

### Questions to be answered (if using the paralympics_raw data set)

To guide the data preparation activity, assume that the questions to answer from the data set are:

- How has the number of male and female competitors in the paralympics changed over time?
- Does the ratio of male:female competitors vary between winter and summer olympics?

In addition to the charts that will attempt to answer the questions, the web app will also feature a searchable history of paralympic events with information about each event.
The event information will include the country flag, the paralympic logo, start and end dates and the duration of the event.

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

- Create a new python code file. 
- Add a line to import pandas as pd 
- Add a line of code to create a dataframe by reading the file from csv

Hint: Use [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) infers the column names from the first row by default.

If you are using your own data set in .xlsx format then refer to [pandas.read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)


## Further practice

There are other data sets in the repository that you could try to prepare for a specific purpose e.g.

1. Prepare the [assembly-london-2012-ticket-sales.xlsx](data/assembly-london-2012-ticket-sales.xls) data such that you
   could use it to later recreate the cycling chart shown on page 14 of the report
   titled [The Price of Gold: Lessons from the London 2012 ticket sales](https://www.london.gov.uk/sites/default/files/gla_migrate_files_destination/Economy%20Committee%20-%20The%20Price%20of%20Gold.pdf)
2. Prepare the [paralympic medal tables data set](data/paralympic_medal_tables.xlsx) to show how a particular country (
   pick any) medal performance has changed over the years.
