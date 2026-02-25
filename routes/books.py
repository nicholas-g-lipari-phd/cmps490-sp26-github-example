from flask import Blueprint, jsonify, request

from services.books_service import get_all_books

books_bp = Blueprint("books", __name__)


@books_bp.get("/api/books")
def search_books():
    title = request.args.get("title", "")
    if title:
        return jsonify({"title": title, "items": []})

    return jsonify(get_all_books())


@books_bp.get("/api/books/<book_id>")
def get_book(book_id):
    # TODO: call service and return details
    return jsonify({"id": book_id})
