import os
from flask import Flask, render_template

def create_app(test_config=None):
    # Create and configure the app
    application = Flask(__name__, instance_relative_config=True)
    app=application
    app.config.from_mapping(
        DATABASE_URL = "PostgreURL"
    )
    
    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Assert the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # App entry point
    @app.route('/')
    def home():
        return render_template('index.html')

    return app

if __name__ == '__main__':
    create_app().run(debug=True)