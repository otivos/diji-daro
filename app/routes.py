from flask import render_template, jsonify
from models import *

def init_routes(app):

    @app.route("/") 
    def home():
        students = Student.query.all()
        for row in students:
            print(row.username)
        return render_template('index.html', students=students)
    
    @app.route("/daro", methods=["GET"])
    def get_api_base_url():
        return jsonify({
            "msg": "digi-daro app is up",
            "success": True,
            "data": None
        }), 200