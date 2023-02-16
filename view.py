from flask import make_response, abort
from model import db, Todo
from schema import todo_schema, todos_schema

def index():
    todos = Todo.query.all()
    return todos_schema.dump(todos)

def create(todo):
    new_todo = todo_schema.load(todo, session=db.session)
    db.session.add(new_todo)
    db.session.commit()
    return todo_schema.dump(new_todo), 201

def show(id):
    selected_todo = Todo.query.filter(Todo.id == id).one_or_none()
    if selected_todo:
        return todo_schema.dump(selected_todo)
    else:
        abort(404, f"Todo with id {id} not found")

def update_text(id, todo):
    selected_todo = Todo.query.filter(Todo.id == id).one_or_none()
    if selected_todo:
        updated_todo = todo_schema.load(todo, session=db.session)
        selected_todo.text = updated_todo.text
        db.session.merge(selected_todo)
        db.session.commit()
        return todo_schema.dump(selected_todo), 201
    else:
        abort(404, f"Todo with id {id} not found")

def update_status(id, todo):
    selected_todo = Todo.query.filter(Todo.id == id).one_or_none()
    if selected_todo:
        updated_todo = todo_schema.load(todo, session=db.session)
        selected_todo.completed = updated_todo.completed
        db.session.merge(selected_todo)
        db.session.commit()
        return todo_schema.dump(selected_todo), 201
    else:
        abort(404, f"Todo with id {id} not found")

def delete(id):
    selected_todo = Todo.query.filter(Todo.id == id).one_or_none()
    if selected_todo:
        db.session.delete(selected_todo)
        db.session.commit()
        return make_response(f"Todo with id {id} deleted successfully")
    else:
        abort(404, f"Todo with id {id} not found")
