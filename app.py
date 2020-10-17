"""




"""

from flask import Flask, render_template, url_for, request, redirect
from apiquery import APIQuery 

news = APIQuery('6868852668184abea077fa547303028a')
app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
    if(request.method == "POST"):
        try:
            query = request.form['query']
            category = request.form['category']
        except Exception as e:
            print(e)
            return "<h1> You were missing some fields </h1>"
        return redirect(url_for("results",query=query, category=category ))
    else:

        return render_template("index.html")

@app.route("/results/<query>/<category>", methods=["GET"])
def results(query, category):
    results = news.search(query, category)
    if(results == []):
        return "<h1> Sorry, no articles were found with these search terms </h1>"
        return "HELLO"
    else:
        return f"<h1> {results[0]['title']}</h1>"


    
     


if __name__ == '__main__':
    app.run()