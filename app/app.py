from models import db
from flask_migrate import Migrate
from init import create_app

app = create_app()
# bootstrap database migrate commands
db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")