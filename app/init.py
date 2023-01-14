import os
from flask import Flask

from routes import init_routes

def create_app(test_config=None):
    # Create and configure the app
    application = Flask(__name__, instance_relative_config=True)
    app=application
    app.config.from_mapping(
        SECRET_KEY = "some_dev_key",
        SQLALCHEMY_DATABASE_URI = "postgresql://usr:pwd@pgsql:5432/daro"
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Assert that the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    init_routes(app)

    return app