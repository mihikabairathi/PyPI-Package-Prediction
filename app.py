# -*- coding: utf-8 -*-
"""
This program creates a website to return dates for any project 
target input
"""

from flask import Flask, request, render_template
from sklearn.externals import joblib
from pynverse import inversefunc
import numpy as np
from datetime import date, timedelta

#load model from file
predictor = joblib.load("pypi_predict_model.pkl")
coefs = predictor.coef_
inverseDate = inversefunc(np.poly1d(coefs[::-1]), domain = [0, 100000000], \
                          open_domain = [False, False])

#load the object
app = Flask(__name__)

#main page when opened
@app.route("/")
def my_form():
    return render_template('page-layout.html')

#main page after input 
@app.route("/", methods = ["POST"])
def whatToDo():
    n = request.form['text']
    ans = ""
    if not n or int(n) < 0 or int(n) > 100000000:
        ans = "Error - you did not enter a valid number!"
    else:
        result = findDate(int(n))
        if int(n) == 1:
            ans = "1 project will be available on PyPI around " + result
        else:
            ans = str(n) + " projects will be available on PyPI around " \
            + result
    return render_template('page-layout.html', message = ans)

#the predicting function
def findDate(num_projects):
    """
    Given the number of projects, this will return the predicted date
    it will be reached
    """
    num_day = int((inverseDate(num_projects)))
    unmodified_date = str((date(2002, 11, 5) + timedelta(days = num_day)))
    mdict = {"01":"Jan", "02":"Feb", "03":"Mar", "04":"Apr", "05":"May", \
             "06":"Jun", "07":"Jul", "08":"Aug", "09":"Sep", "10":"Oct", \
             "11":"Nov", "12":"Dec"}
    return unmodified_date[-2:] + " " + mdict[unmodified_date[-5:-3]] + " " + \
                unmodified_date[0:4]

#running the site
if __name__ == "__main__":
    app.run(port=6500)
