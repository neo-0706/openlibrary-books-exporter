from dataclasses import dataclass


@dataclass
class Book:
    key: str
    title: str
    authors: list[str]
    first_publish_year: int
