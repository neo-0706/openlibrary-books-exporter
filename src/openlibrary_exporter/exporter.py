import csv
from pathlib import Path

from .models import Book


def export_to_csv(books: list[Book], output_file: str | Path) -> None:
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "title",
                "authors",
                "first_publish_year",
                "openlibrary_key",
            ],
        )

        writer.writeheader()

        for book in books:
            writer.writerow(
                {
                    "title": book.title,
                    "authors": ", ".join(book.authors),
                    "first_publish_year": book.first_publish_year,
                    "openlibrary_key": book.key,
                }
            )
