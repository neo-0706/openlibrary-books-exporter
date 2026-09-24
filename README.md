# OpenLibrary Books Exporter

A clean and testable Python utility that fetches book data from the
[Open Library Search API](https://openlibrary.org/developers/api),
filters books published after 2000, sorts the results, and exports
50 books to a CSV file.

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Tests](https://img.shields.io/badge/Tests-pytest-green)
![Linting](https://img.shields.io/badge/Linting-Ruff-orange)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue)

---

## ✨ Features

- Fetches book data from the Open Library Search API
- Uses a focused set of API fields instead of downloading unnecessary data
- Filters books published after 2000
- Sorts results by:
  1. Publication year (ascending)
  2. Title (ascending)
- Exports exactly 50 books to CSV
- Separates API communication, business logic, and CSV exporting
- Includes automated unit tests with `pytest`
- Uses mocked HTTP requests in tests
- Includes Ruff for code quality and formatting
- Runs tests and linting automatically through GitHub Actions

---

## 🏗️ Project Structure

```text
openlibrary-books-exporter/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── src/
│   └── openlibrary_exporter/
│       ├── __init__.py
│       ├── client.py
│       ├── exporter.py
│       ├── main.py
│       ├── models.py
│       └── service.py
│
├── tests/
│   ├── __init__.py
│   ├── test_client.py
│   ├── test_exporter.py
│   └── test_service.py
│
├── output/
│   └── .gitkeep
│
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md

## Architecture
The application follows a simple separation of responsibilities:
```text
    Open Library API
            │
            ▼
    ┌─────────────────┐
    │   API Client    │
    │    client.py    │
    └────────┬────────┘
            │
            ▼
    ┌─────────────────┐
    │  Book Service   │
    │   service.py   │
    └────────┬────────┘
            │
    Filter & Sort
            │
            ▼
    ┌─────────────────┐
    │  CSV Exporter   │
    │  exporter.py   │
    └────────┬────────┘
            │
            ▼
        output/books.csv

## ⚙️ Requirements

* Python 3.11+
* pip

> **Note:** Python 3.14 is used for development and CI.

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/neo-0706/openlibrary-books-exporter.git
cd openlibrary-books-exporter
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate it on Windows

```bash
.venv\Scripts\activate
```

### Activate it on macOS/Linux

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the application with:

```bash
python -m openlibrary_exporter.main
```

The generated CSV file will be available at:

```text
output/books.csv
```

The CSV contains the following columns:

| Column               | Description                  |
| -------------------- | ---------------------------- |
| `title`              | Book title                   |
| `authors`            | Book author(s)               |
| `first_publish_year` | First known publication year |
| `openlibrary_key`    | Open Library work identifier |

## 🧪 Testing

Tests are written using **pytest**.

Run the complete test suite:

```bash
pytest
```

The tests cover:

* Open Library API response handling
* Conversion of API responses into `Book` objects
* HTTP error handling
* Filtering books published after 2000
* Sorting results
* Limiting results to 50 books
* CSV generation and contents

External API calls are mocked in unit tests, making the test suite deterministic and independent of network availability.

## 🔍 Code Quality

The project uses **Ruff** for linting and formatting.

### Run Ruff

```bash
ruff check .
```

### Format the project

```bash
ruff format .
```

## 🔄 Continuous Integration

**GitHub Actions** automatically runs on every push and pull request.

The CI workflow:

1. Sets up Python 3.14
2. Installs project dependencies
3. Runs the test suite
4. Runs Ruff

This helps ensure that changes do not break existing functionality or introduce linting issues.

## 📋 Data Processing Rules

The application follows these rules:

### Publication Year

Only books with:

```text
first_publish_year > 2000
```

are included.

Therefore:

| Year | Included |
| ---- | :------: |
| 2001 |     ✓    |
| 2005 |     ✓    |
| 2020 |     ✓    |
| 2000 |     ✗    |
| 1999 |     ✗    |

### Sorting

Results are sorted by:

```text
first_publish_year ASC
title ASC
```

The title is used as a deterministic tie-breaker when multiple books have the same publication year.

### Result Count

The final exported dataset contains exactly:

```text
50 books
```

## 🧩 Design Decisions

The project intentionally keeps the architecture simple and avoids unnecessary overengineering.

### Why separate the API client?

`client.py` is responsible only for communicating with Open Library and converting API responses into application models.

This keeps HTTP-related concerns away from business logic.

### Why a service layer?

`service.py` contains the application's business rules, such as filtering and sorting.

This makes those rules easy to test independently from the API.

### Why mock API requests?

Unit tests should not depend on:

* Internet connectivity
* Open Library availability
* API response timing
* External service changes

Therefore, HTTP requests are mocked during tests.

## 📦 Dependencies

### Runtime

* `requests`

### Development

* `pytest`
* `ruff`

## 📄 License

This project was created as a software engineering task for educational purposes.
