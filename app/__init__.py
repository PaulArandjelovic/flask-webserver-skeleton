"""Initialize Flask app."""
from flask import Flask


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        from .profile import profile
        from .home import home

        # Register Blueprints
        app.register_blueprint(profile.profile_bp)
        app.register_blueprint(home.home_bp)

        return app
