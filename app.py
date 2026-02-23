from flask import Flask


def create_app():
    """
    Create and configure a Flask application for book search.
    This factory function initializes a Flask application instance with:
    - A root route handler that serves a basic HTML page with a "Book Search" title
    - Placeholder for blueprint registration (to be implemented)
    Returns:
        Flask: A configured Flask application object ready to run.
    """
    app = Flask(__name__)

    @app.get("/")
    def index():
        return "<!DOCTYPE html><html><head><title>Book Search</title></head><body><h1>Book Search</h1></body></html>"

    # TODO: register blueprints

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
