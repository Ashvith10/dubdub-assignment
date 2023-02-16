import os
import connexion
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from model import db
from schema import ma

connex_app = connexion.App(__name__)
connex_app.add_api('swagger.yml')
app = connex_app.app
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def validate_database():
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(engine.url):
        create_database(engine.url)
        print("New Database Created")
    else:
        print("Database Already Exists")

@app.before_first_request
def create_tables():
    validate_database()
    db.create_all()

db.init_app(app)
ma.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
