from flask import render_template, jsonify

def init_routes(app):

    @app.route("/")
    def home():
        return render_template('index.html')
    
    @app.route("/daro", methods=["GET"])
    def get_api_base_url():
        return jsonify({
            "msg": "digi-daro app is up",
            "success": True,
            "data": None
        }), 200