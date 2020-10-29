"""
File Name: app.py
Author: Akli Amrous
Description: This is a flask server that allows
ease of use for the News API and dynamic rendering

Copyright (c) Akli Amrous 2020

"""

from flask import Flask, render_template, url_for, request, redirect
from apiquery import APIQuery 


news = APIQuery('78b9d599c4f94f8fa3afb1a5458928d6')
app = Flask(__name__)
app.secret_key="akliamrous"


@app.route('/', methods=["POST", "GET"])
def home():
    if(request.method == "POST"):
        try:
            query = request.form['query']  
            category = request.form['category']
            print(category)
            if(query  == ""):
                return redirect(url_for("failed"))
            
            return redirect(url_for("results", query=query, category=category ))
            
            # The user must fill all fields or else the app cannot work
        except Exception as e: 
            return redirect(url_for("failed"))
        
    else:

        return render_template("index.html")

@app.route("/results/<query>/<category>", methods=["GET"])
def results(query, category):
    check = news.search(query, category)['articles']
    results = news.parse(news.search(query, category))
    length = len(results['sources'])
    data = (results, length)
    if(check == []):

        return redirect(url_for("notfound"))
    else:
        return render_template("results.html", data=data)


@app.route("/failed", methods=["GET"])
def failed():
    return render_template("failed.html")


@app.route("/notfound", methods=["GET"])
def notfound():
    return render_template("notfound.html")

if __name__ == '__main__':
    app.run()
