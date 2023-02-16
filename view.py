from flask import make_response, abort
from model import db, Task
from schema import task_schema, tasks_schema

def index():
    tasks = Task.query.order_by(Task.id.asc())
    return tasks_schema.dump(tasks)

def create(task):
    new_task = task_schema.load(task, session=db.session)
    db.session.add(new_task)
    db.session.commit()
    return task_schema.dump(new_task), 201

def show(id):
    selected_task = Task.query.filter(Task.id == id).one_or_none()
    if selected_task:
        return task_schema.dump(selected_task)
    else:
        abort(404, f"Task with id {id} not found")

def update_text(id, task):
    selected_task = Task.query.filter(Task.id == id).one_or_none()
    if selected_task:
        updated_task = task_schema.load(task, session=db.session)
        selected_task.text = updated_task.text
        db.session.merge(selected_task)
        db.session.commit()
        return task_schema.dump(selected_task), 201
    else:
        abort(404, f"Task with id {id} not found")

def update_status(id, task):
    selected_task = Task.query.filter(Task.id == id).one_or_none()
    if selected_task:
        updated_task = task_schema.load(task, session=db.session)
        selected_task.completed = updated_task.completed
        db.session.merge(selected_task)
        db.session.commit()
        return task_schema.dump(selected_task), 201
    else:
        abort(404, f"Task with id {id} not found")

def delete(id):
    selected_task = Task.query.filter(Task.id == id).one_or_none()
    if selected_task:
        db.session.delete(selected_task)
        db.session.commit()
        return make_response(f"Task with id {id} deleted successfully")
    else:
        abort(404, f"Task with id {id} not found")
