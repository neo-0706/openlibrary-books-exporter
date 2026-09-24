import requests

from .models import Book


class OpenLibraryClient:
    def __init__(
        self,
        base_url: str = "https://openlibrary.org/search.json",
        timeout: float = 10.0,
        user_agent: str = "openlibrary-books-exporter/0.1.0",
    ):
        self.base_url = base_url
        self.timeout = timeout
        self.user_agent = user_agent

    def search_books(self, query: str, limit: int, page: int = 1) -> list[Book]:
        params = {
            "q": query,
            "fields": "key,title,author_name,first_publish_year",
            "limit": limit,
            "page": page,
        }

        headers = {
            "User-Agent": self.user_agent,
        }

        response = requests.get(
            self.base_url,
            params=params,
            headers=headers,
            timeout=self.timeout,
        )
        response.raise_for_status()

        data = response.json()

        books = []

        for doc in data.get("docs", []):
            if "first_publish_year" not in doc:
                continue

            book = Book(
                key=doc.get("key", ""),
                title=doc.get("title", ""),
                authors=doc.get("author_name", []),
                first_publish_year=doc["first_publish_year"],
            )

            books.append(book)

        return books
