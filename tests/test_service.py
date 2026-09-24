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