# -*- coding: utf-8 -*-
"""
This program takes the cleaned PyPI data and tabulates it.
For an EDA of the data, refer to the .ipynb notebook.
"""
import pandas as pd

df = pd.read_csv('cleaned_project_and_date.csv')
df = df.drop("Unnamed: 0", axis = 1)

#extracting useful information and modifying it
useful_df = pd.DataFrame()
useful_df["Project Name"] = df.name
useful_df["Release Date"] = pd.to_datetime(df.old_date)
useful_df = useful_df.sort_values(by = "Release Date")
useful_df = useful_df.reset_index()

#number of projects released on that day
num_df = useful_df.groupby("Release Date").agg({"Project Name": "count"})

#range of dates
final_df = pd.DataFrame()
final_df["Release Date"] = pd.Series(pd.date_range(start = "2002-11-05", \
        end = "2019-07-18", freq = "d"))

#merging tables to create final one
final = pd.merge(final_df, num_df, on = "Release Date", how = "left")
final = final.fillna(0)
final["On Day"] = final["Project Name"]
final = final.drop("Project Name", axis = 1)
final = final.set_index("Release Date")
temp = final.cumsum(axis = 0)
final["So Far"] = temp["On Day"]
