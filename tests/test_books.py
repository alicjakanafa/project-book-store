from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection
from book_repository import BookRepository, Book

def test_book_list_contains_all_book_details(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books_store.sql")
    page.goto("http://127.0.0.1:5001/books")

    titles = page.locator(".book-title")
    authors = page.locator(".book-author")
    years = page.locator(".book-year")

    expect(titles).to_have_text([
        "The Great Gatsby",
        "To Kill a Mockingbird",
        "1984",
        "Pride and Prejudice",
        "The Catcher in the Rye",
        "Project Hail Mary"
    ])

    expect(authors).to_have_text([
        "By F. Scott Fitzgerald",
        "By Harper Lee",
        "By George Orwell",
        "By Jane Austen",
        "By J.D. Salinger",
        "By Andy Weir"
    ])

    expect(years).to_have_text([
        "Published: 1925",
        "Published: 1960",
        "Published: 1949",
        "Published: 1813",
        "Published: 1951",
        "Published: 2021"
    ])

def test_user_can_add_a_new_book(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books_store.sql")

    # Log in
    page.goto("http://127.0.0.1:5001/sessions/new")

    page.get_by_label("Username").fill("akanafa")
    page.get_by_label("Password").fill("12345")

    page.get_by_role("button", name="Log In").click()

    expect(page).to_have_url(
        "http://127.0.0.1:5001/books"
    )

    # Go to the new Add Book page
    page.goto("http://127.0.0.1:5001/books/new")

    expect(page).to_have_url(
        "http://127.0.0.1:5001/books/new"
    )

    # Fill in the form
    page.get_by_label("Title").fill(
        "Before the Coffee Gets Cold"
    )

    page.get_by_label("Author").fill(
        "Toshikazu Kawaguchi"
    )

    page.get_by_label("Year").fill("2019")

    page.get_by_role(
        "button",
        name="Add Book"
    ).click()

    # POST /books redirects back to the list
    expect(page).to_have_url(
        "http://127.0.0.1:5001/books"
    )

    expect(
        page.get_by_text(
            "Before the Coffee Gets Cold",
            exact=True
        )
    ).to_be_visible()

    expect(
        page.get_by_text(
            "By Toshikazu Kawaguchi",
            exact=True
        )
    ).to_be_visible()

    expect(
        page.get_by_text(
            "Published: 2019",
            exact=True
        )
    ).to_be_visible()

def test_search_books_by_title():
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books_store.sql")

    repository = BookRepository(connection)

    books = repository.search(title="Gatsby")

    assert books == [
        Book(
            "The Great Gatsby",
            "F. Scott Fitzgerald",
            1925,
            1
        )
    ]

def test_search_books_by_year():
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books_store.sql")

    repository = BookRepository(connection)

    books = repository.search(year="1949")

    assert books == [
        Book(
            "1984",
            "George Orwell",
            1949,
            3
        )
    ]

def test_user_can_filter_books_by_title(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books_store.sql")

    page.goto("http://127.0.0.1:5001/books")

    page.get_by_label("Search by title").fill("Gatsby")
    page.get_by_role("button", name="Search").click()

    expect(page.locator(".book-card")).to_have_count(1)

    expect(
        page.get_by_text("The Great Gatsby", exact=True)
    ).to_be_visible()

    expect(
        page.get_by_text("1984", exact=True)
    ).not_to_be_visible()