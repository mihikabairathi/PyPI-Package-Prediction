# -*- coding: utf-8 -*-
"""
This program cleans up the data scraped by "pypi web scraping.py"
and saves it in a csv file.
"""

import pandas as pd

def change_month_to_number(datestr):
    """ 
    converts date string to string without text, just numbers
    """
    mdict = {"Jan":'1', "Feb":'2', "Mar":'3', "Apr":'4', "May":'5', "Jun":'6',\
        "Jul":'7', "Aug":'8', "Sep":'9', "Oct":'10', "Nov":'11', "Dec":'12'}
    return mdict[datestr[:3]] + datestr[3:]

#creates initial columns in dataframe
df = pd.read_csv('project_and_date.csv')
df.loc[-1] = ['0', [('0.0.0', 'Aug 6, 2017')], '0.1']  # adding a row
df.index = df.index + 1  # shifting index
df.sort_index(inplace=True) 
df.columns = ['name', 'version and date', 'description']
df['version and date'] = df['version and date'].astype(str)
df = df.drop_duplicates()
old_dates = pd.Series(index = range(len(df.description)))
num_versions = pd.Series(index = range(len(df.description)))
all_versions = pd.Series(index = range(len(df.description)))
all_dates = pd.Series(index = range(len(df.description)))

#extracting dates, versions
for i, l in df['version and date'].iteritems():
    index = l[:-3].rfind('\'')
    old_dates[i] = l[index+1:-3]
    num_versions[i] = l.count('(')
    list_of_tuples = l.split('\'')
    list_of_tuples = list_of_tuples[1::2]
    all_dates[i] = list_of_tuples[1::2]
    all_versions[i] = list_of_tuples[::2]

#date formatting
for i, date in old_dates.iteritems():
    old_dates[i] = pd.to_datetime(change_month_to_number(date), format = \
             "%m %d, %Y")
    
for i, datelist in all_dates.iteritems():
    for i in range(len(datelist)):
        datelist[i] = pd.to_datetime(change_month_to_number(date), format = \
             "%m %d, %Y")
    all_dates[i] = datelist

#final dataframe
final_df = pd.DataFrame()
final_df['name'] = df.name.astype(str)
final_df['old_date'] = old_dates
final_df['num_versions'] = num_versions.astype(int)
final_df['all_versions'] = all_versions
final_df['all_dates'] = all_dates
final_df['description'] = df.description.astype(str)
final_df['description'] = final_df['description'].fillna("")

final_df.to_csv('cleaned_project_and_date.csv')
