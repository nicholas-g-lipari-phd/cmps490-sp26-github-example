import json
from pathlib import Path


def load_books():
    data_path = Path(__file__).resolve().parents[1] / "data" / "books.json"
    with data_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_all_books():
    return load_books()


def search_books_by_title(title):
    # TODO: implement filtering in Stage 4
    return load_books()


def get_book_by_id(book_id):
    # TODO: load details from static data or external API
    return None
