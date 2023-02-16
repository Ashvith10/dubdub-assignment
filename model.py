from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Todo(db.Model):
    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    completed = db.Column(db.Boolean)

    def __repr__(self):
        return '<Todo %r>' % self.text
