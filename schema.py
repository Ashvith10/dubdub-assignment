from flask_marshmallow import Marshmallow
from model import Task, db
ma = Marshmallow()

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        load_instance = True
        sqla_session = db.session

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
