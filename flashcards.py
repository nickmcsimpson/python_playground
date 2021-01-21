from flask import Flask, render_template, abort, jsonify
from datetime import datetime

from model import db

app = Flask(__name__)
# export FLASK_APP=flashcards.py
# export FLASK_ENV=development

"""
>>> import flashcards
>>> flashcards.app.url_map
Map([<Rule '/load_counter' (GET, HEAD, OPTIONS) -> load_counter>,
 <Rule '/date' (GET, HEAD, OPTIONS) -> date>,
 <Rule '/' (GET, HEAD, OPTIONS) -> welcome>,
 <Rule '/static/<filename>' (GET, HEAD, OPTIONS) -> static>])

"""


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        cards=db,
    )

@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())

#global
count = 0


@app.route("/load_counter")
def count_demo():#name is irrelevant to route
    global count
    count += 1
    return f"We loaded this page {count} times"


@app.route("/card")
def card_default():
    return card_view(0)


@app.route("/card/<int:index>")#parameter format
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", 
                                card=card,
                                index=index,
                                max_index=len(db)-1
                                )
    except IndexError:
        abort(404)


@app.route("/api/card/")
def api_card_list():
    return jsonify(db)


@app.route('/api/card/<int:index>')
def api_card_detail(index):
    try:
        return db[index] #automatically serialized and returned as JSON
    except IndexError:
        abort(404)
