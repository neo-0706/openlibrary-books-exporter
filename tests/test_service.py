from openlibrary_exporter.models import Book
from openlibrary_exporter.service import BookService


def test_get_books_filters_books_published_after_2000():
    # Arrange
    books = [
        Book(
            key="/works/1",
            title="Old Book",
            authors=["Author"],
            first_publish_year=1999,
        ),
        Book(
            key="/works/2",
            title="New Book",
            authors=["Author"],
            first_publish_year=2005,
        ),
    ]

    # Act
    service = BookService(books)
    result = service.get_books()

    # Assert
    assert len(result) == 1
    assert result[0].title == "New Book"

def test_get_books_sorts_and_limits_results():
    # Arrange
    books = [
        Book("/works/1", "Zebra", ["Author"], 2005),
        Book("/works/2", "Apple", ["Author"], 2003),
        Book("/works/3", "Book", ["Author"], 2003),
        Book("/works/4", "Old Book", ["Author"], 1999),
    ]

    service = BookService(books)

    # Act
    result = service.get_books()

    # Assert
    assert len(result) == 3
    assert result[0].title == "Apple"
    assert result[1].title == "Book"
    assert result[2].title == "Zebra"