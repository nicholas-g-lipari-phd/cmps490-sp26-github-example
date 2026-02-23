from flask import Blueprint, jsonify, request

books_bp = Blueprint("books", __name__)


@books_bp.get("/api/books")
def search_books():
    title = request.args.get("title", "")
    # TODO: call service and return results
    return jsonify({"title": title, "items": []})


@books_bp.get("/api/books/<book_id>")
def get_book(book_id):
    # TODO: call service and return details
    return jsonify({"id": book_id})
