from flask_marshmallow import Marshmallow
from model import Todo, db
ma = Marshmallow()

class TodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Todo
        load_instance = True
        sqla_session = db.session

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)
