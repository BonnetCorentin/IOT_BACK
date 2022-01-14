from flask import json

from APP import db


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Localisation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.String(100), unique=True)
    longitude = db.Column(db.String(100))
    date = db.Column(db.String(100))

    def __init__(self, latitude, longitude, date):
        self.latitude = latitude
        self.longitude = longitude
        self.date = date

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            # This is an example how to deal with Many2Many relations
            # 'many2many': self.serialize_many2many
            'date': self.date
        }

    @property
    def serialize_many2many(self):
        """
        Return object's relations in easily serializable format.
        NB! Calls many2many's serialize property.
        """
        return [item.serialize for item in self.many2many]
