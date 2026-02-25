from datetime import datetime, timezone
import json
from pathlib import Path

from flask import Flask, jsonify, render_template, request

from routes.books import books_bp


def create_app():
    """
    Create and configure a Flask application for book search.
    This factory function initializes a Flask application instance with:
    - Placeholder for blueprint registration (to be implemented)
    Returns:
        Flask: A configured Flask application object ready to run.
    """
    app = Flask(__name__)

    def load_books():
        data_path = Path(app.root_path) / "data" / "books.json"
        with data_path.open("r", encoding="utf-8") as file:
            return json.load(file)

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

    @app.get("/ping")
    def ping_viewer():
        return render_template("ping.html")

    app.register_blueprint(books_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
