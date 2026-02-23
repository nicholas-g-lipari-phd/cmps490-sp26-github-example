from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def index():
        return "<!DOCTYPE html><html><head><title>Book Search</title></head><body><h1>Book Search</h1></body></html>"

    # TODO: register blueprints

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
