import csv

from openlibrary_exporter.exporter import export_to_csv
from openlibrary_exporter.models import Book


def test_export_to_csv(tmp_path):
    books = [
        Book(
            key="/works/1",
            title="The Hobbit",
            authors=["J. R. R. Tolkien"],
            first_publish_year=1937,
        ),
    ]

    output_file = tmp_path / "books.csv"

    export_to_csv(books, output_file)

    with open(output_file, newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert len(rows) == 1
    assert rows[0]["title"] == "The Hobbit"
    assert rows[0]["authors"] == "J. R. R. Tolkien"
    assert rows[0]["first_publish_year"] == "1937"
    assert rows[0]["openlibrary_key"] == "/works/1"
