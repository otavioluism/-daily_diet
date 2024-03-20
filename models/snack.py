from database import db

class Snack(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False, unique=True)
  description = db.Column(db.String(120), nullable=False)
  timestamp = db.Column(db.Date, nullable=False)
  diet = db.Column(db.Boolean, nullable=False)
  