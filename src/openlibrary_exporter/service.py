from .models import Book


class BookService:
    def __init__(self, books: list[Book]):
        self.books = books

    def get_books(self) -> list[Book]:
        result = [
            book
            for book in self.books
            if book.first_publish_year > 2000
        ]

        result.sort(key=lambda book: (book.first_publish_year, book.title))

        return result[:50]