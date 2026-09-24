from unittest.mock import Mock, patch

import pytest
import requests

from openlibrary_exporter.client import OpenLibraryClient
from openlibrary_exporter.models import Book


def test_search_books_returns_books():
    # Arrange
    fake_response = Mock()

    fake_response.json.return_value = {
        "docs": [
            {
                "key": "/works/OL123W",
                "title": "The Hobbit",
                "author_name": ["J. R. R. Tolkien"],
                "first_publish_year": 1937,
            }
        ]
    }

    # Act
    with patch("openlibrary_exporter.client.requests.get") as mock_get:
        mock_get.return_value = fake_response

        client = OpenLibraryClient()
        books = client.search_books("The Hobbit", 1)

    # Assert
    assert len(books) == 1
    assert isinstance(books[0], Book)
    assert books[0].title == "The Hobbit"


def test_search_books_raises_for_http_error():
    # Arrange
    fake_response = Mock()
    fake_response.raise_for_status.side_effect = requests.HTTPError

    # Act & Assert
    with patch("openlibrary_exporter.client.requests.get") as mock_get:
        mock_get.return_value = fake_response

        client = OpenLibraryClient()

        with pytest.raises(requests.HTTPError):
            client.search_books("The Hobbit", 1)
