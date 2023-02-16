from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    completed = db.Column(db.Boolean)

    def __repr__(self):
        return '<Task %r>' % self.text
