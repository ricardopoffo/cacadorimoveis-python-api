from flask import Flask
from app.config import Config
from app.extensions import db
from app.main import bp as main_bp
from app.scrap.scrap import scrap_bp
from app.real_estate.real_estate import real_estate_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    app.register_blueprint(main_bp)
    app.register_blueprint(scrap_bp, url_prefix='/scrap')
    app.register_blueprint(real_estate_bp, url_prefix='/real-estate')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app