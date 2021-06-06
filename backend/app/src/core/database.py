from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from src.core.flask_app import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)
