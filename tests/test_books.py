from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection

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

    # Log in first
    page.goto("http://127.0.0.1:5001/sessions/new")

    page.get_by_label("Username").fill("akanafa")
    page.get_by_label("Password").fill("12345")

    page.get_by_role("button", name="Log In").click()

    # Successful login redirects us to /books
    expect(page).to_have_url("http://127.0.0.1:5001/books")

    # Now add the book
    page.get_by_label("Title").fill("Before the Coffee Gets Cold")
    page.get_by_label("Author").fill("Toshikazu Kawaguchi")
    page.get_by_label("Year").fill("2019")

    page.get_by_role("button", name="Add Book").click()

    expect(page.get_by_text("Before the Coffee Gets Cold", exact=True)).to_be_visible()
    expect(page.get_by_text("By Toshikazu Kawaguchi", exact=True)
    ).to_be_visible()
    expect(page.get_by_text("Published: 2019", exact=True)
    ).to_be_visible()