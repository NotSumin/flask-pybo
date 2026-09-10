from flask import Flask
from flask_migrate import Migrate, migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

# application factory
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # initialize ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # @app.route('/')
    # def hello_pybo():
    #     return 'Hello Pybo~!'
    #
    # @app.route('/hello')
    # def hello():
    #     return 'hello page입니다!'

    # blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app