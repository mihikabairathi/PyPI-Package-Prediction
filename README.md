# PyPI-Package-Prediction

This project builds upon details of all the projects currently uploaded on 
"https://pypi.org/" to create a model that can predict a date for when 
a certain number of projects/packages uploaded on the website could be reached.

### Motivation
This project was developed to guide anyone to learn different aspects of Data 
Science – collection of data, exploratory data analysis (EDA), predictive models 
using ML algorithms, and deployment of a model - all while creating an application
with practical use.

### Prerequisites
This entire project is programmed in Python 3. The different modules used are:
1. BeautifulSoup4 (bs4)
2. requests
3. csv
4. tqdm
5. re
6. codecs
7. pandas
8. matplotlib
9. sklearn
10. flask
11. pynvrese
12. numpy
13. datetime

All these modules can be installed by the "pip install" command.

### Instructions for using the model
To use just the final web service, download the files "pypi_predict_model.pkl",  
"templates", and "app.py", and execute the program. Then, type in "localhost:6500" in your
browser to access the website created.

### Files (code)
Here is a list of all the python files in the project:
1. "pypi web scraping.py": scrapes the data of all the projects on the
website with the help of "https://pypi.org/simple/", a site that lists
the names of all the uploaded projects.
2. "pypi data cleaning.py": cleans up the data scraped above.
3. "PyPI Data Analysis (22nd July).ipynb": performs an EDA on the clean data.
4. "polynomial regression pypi.py": a polynomial regression model is 
created by training it on part of the data available, so that it can predict
future dates as well.
5. "app.py": develops a website that provides a simple interface to use the
model created.

### Other Files
Here is a list of all the other files in the project:
1. "project_and_date.csv": all the projects with their names, versions, 
release dates, and descriptions, scraped by "pypi web scraping.py".
2. "cleaned_project_and_date.csv": data cleaned by "pypi data cleaning.py".
3. "pypi_predict_model.pkl": pickled file of the regression model.
4. "page-layout.html": corresponding HTML file for "app.py", stored in 
the "templates directory"
