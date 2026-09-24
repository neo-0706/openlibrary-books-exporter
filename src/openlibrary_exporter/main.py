from openlibrary_exporter.client import OpenLibraryClient
from openlibrary_exporter.exporter import export_to_csv
from openlibrary_exporter.service import BookService


def main():
    client = OpenLibraryClient()

    books = []

    for page in range(1, 6):
        books.extend(client.search_books("book", 100, page=page))

    service = BookService(books)
    books = service.get_books()

    if len(books) < 50:
        raise RuntimeError("Could not find 50 books published after 2000.")

    export_to_csv(books[:50], "output/books.csv")


if __name__ == "__main__":
    main()
