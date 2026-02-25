from flask import Blueprint, jsonify, request

from services.books_service import search_books_by_title

books_bp = Blueprint("books", __name__)


@books_bp.get("/api/books")
def search_books():
    title = request.args.get("title", "")
    return jsonify(search_books_by_title(title))


@books_bp.get("/api/books/<book_id>")
def get_book(book_id):
    # TODO: call service and return details
    return jsonify({"id": book_id})
