from datetime import datetime, timezone

from flask import Flask, jsonify, render_template, request


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
        return render_template("index.html")

    @app.get("/api/ping")
    def api_ping():
        return jsonify(
            {
                "status": "ok",
                "message": "API reachable",
                "server_time": datetime.now(timezone.utc).isoformat(),
                "user_agent": request.headers.get("User-Agent", ""),
                "client_ip": request.remote_addr,
                "method": request.method,
            }
        )

    # TODO: register blueprints

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
