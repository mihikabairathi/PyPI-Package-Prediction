# -*- coding: utf-8 -*-
"""
This program extracts the required data from the PyPI data collected and
then creates a model that can be used to predict a date for which an
input of the number of projects published can be achieved.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.externals import joblib

#extracting useful information and modifying it
df = pd.read_csv('C:/Users/mihik/.spyder-py3/Diconium Internship/Week 2/' + \
          'week 2 pypi/cleaned_project_and_date.csv')
df = df.drop("Unnamed: 0", axis = 1)
useful_df = pd.DataFrame()
useful_df["Project Name"] = df.name
useful_df["Release Date"] = pd.to_datetime(df.old_date)
useful_df = useful_df.sort_values(by = "Release Date")
useful_df = useful_df.reset_index()

#number of projects released on that day
random_df = useful_df.groupby("Release Date").agg({"Project Name": "count"})

#range of dates
final_df = pd.DataFrame()
final_df["Release Date"] = pd.Series(pd.date_range(start = "2002-11-05", \
        end = "2019-07-18", freq = "d"))

#merging tables to create final one
final = pd.merge(final_df, random_df, on = "Release Date", how = "left")
final = final.fillna(0)
final["On Day"] = final["Project Name"]
final = final.drop("Project Name", axis = 1)
final = final.set_index("Release Date")
temp = final.cumsum(axis = 0)
final["So Far"] = temp["On Day"]
final = final.drop("On Day", axis = 1)
final = final.reset_index()
final = final.drop("Release Date", axis = 1)
final["Day Num"] = pd.Series(range(len(final["So Far"])))

#test and train data
X = final.drop("So Far", axis = 1)
y = final["So Far"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, \
                                    random_state=0, shuffle = False)

#fitting Polynomial Regression to the dataset
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X_train)
pol_reg = LinearRegression()
pol_reg.fit(X_poly, y_train)

#visualizing the Polymonial Regression results
def viz_polymonial():
    plt.figure(figsize=(12, 12))
    plt.plot(X, y, color='red')
    plt.plot(X_test, pol_reg.predict(poly_reg.fit_transform(X_test)), \
             color='blue')
    plt.title('Prediction')
    plt.xlabel('Day Number')
    plt.ylabel('Number of Projects')
    plt.legend()
    plt.show()
    return

viz_polymonial()

#pickle, save the data
joblib.dump(pol_reg, "pypi_predict_model.pkl")

