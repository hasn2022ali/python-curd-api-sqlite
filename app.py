from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from controllers import user_bp



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(user_bp, url_prefix='/api')

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)