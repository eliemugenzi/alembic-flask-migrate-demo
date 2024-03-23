import datetime
from ...app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    created_at = db.Column(db.DateTime)