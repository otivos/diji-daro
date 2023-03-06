import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_session import Session

def create_app(test_config=None):
    
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config["SECRET_KEY"] = "some_dev_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config['UPLOADS_FOLDER'] = 'static/uploads'
    app.config['UPLOAD_EXTENSIONS'] = '.pdf'
    app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
    
    @app.errorhandler(413)
    def request_entity_too_large(error):
        return jsonify({'error': 'Mbaya sana'}), 413
    
    # configure sessions.
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = 'filesystem'
    Session(app)

    import auth
    app.register_blueprint(auth.bp)

    import student
    app.register_blueprint(student.bp)
    app.add_url_rule('/', endpoint='index')

    import uploads
    app.register_blueprint(uploads.bp)
    
    return app