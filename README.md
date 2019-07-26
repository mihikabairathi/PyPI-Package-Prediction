# PyPI-Package-Prediction

This project aims to predict when the number of projects uploaded on PyPI 
reaches 200,000, by looking at the number of projects currently uploaded, and 
the dates when the first versions of these projects were uploaded. 

This project was started to learn about the different aspects of data science
and apply the skills learnt.

A list of all PyPI project names was scraped from 'https://pypi.org/simple/'.

In the file 'project_and_date.csv', a list of all the project names along with 
details such as versions, release dates, and description is stored, after 
scraping it off 'https://pypi.org/'. This is done using the Python modules 
BeautifulSoup and Requests, in the file "pypi web scraping.py".

In the file 'cleaned_project_and_date.csv', a cleaned version of this data is 
stored, using the Python module Pandas. It has separate columns for - name, 
oldest release date, all the release dates, number of project versions, 
all the project versions, and a description. This is done in the file
"pypi data cleaning.py".

In the file "pypi data analysis.py", the cleaned data is organised into a table
and then several trends are analysed in the corresponding notebook, 
"PyPI Data Analysis (22nd July).ipynb".

In the file "polynomial regression pypi.py", a polynomial regression algorithm
using the module sklearn is used to model the given data and then predict 
future values. This model is pickled and stored in "pypi_predict_model.pkl".

Finally, in "app.py", this model is deployed on a website, where the user can 
enter the number of projects, and the model will predict the date this will be 
achieved. The corresponding HTML file for this is "page-layout.html", stored in 
the "templates" directory.

The two CSV files are stored in your local computer and/or andrew google drive.
