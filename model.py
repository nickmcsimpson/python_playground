"""
model.py
-------
Implements the model for our site by simulating a database

Note: although this works as an example this won't be used in production.
sqlalchemy is a way to do this for real
"""

import json


def load_db():
    with open("flashcards_db.json") as f:
        return json.load(f)


def save_db():
    with open("flashcards_db.json", "w") as f:
        return json.dump(db,f)

db = load_db()