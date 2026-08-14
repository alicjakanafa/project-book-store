# in a new file called test_auth.py
from app import app
from database_connection import DatabaseConnection
from playwright.sync_api import Page, expect

def test_auth_integration():
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    response = client.post('/sessions', data={
        'username': 'test',
        'password': '1234'
    })

    assert response.status_code == 302
    # this assertion might be new to you :)
    assert response.headers['Location'].endswith('/books')

def test_auth_playwright(page: Page):

    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_placeholder("Username").fill("test")
    page.get_by_placeholder("Password").fill("1234")
    page.get_by_role("button", name="Log In").click()
    print(page.url)

    expect(page).to_have_url("http://localhost:5001/books")

def test_logged_out_user_cannot_access_add_book_page(page: Page):
    page.goto("http://127.0.0.1:5001/books/new")

    expect(page).to_have_url(
        "http://127.0.0.1:5001/sessions/new"
    )

def test_logged_in_user_can_access_add_book_page(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books_store.sql")

    page.goto("http://127.0.0.1:5001/sessions/new")

    page.get_by_label("Username").fill("akanafa")
    page.get_by_label("Password").fill("12345")
    page.get_by_role("button", name="Log In").click()

    page.goto("http://127.0.0.1:5001/books/new")

    expect(
        page.get_by_role("heading", name="Add a Book")
    ).to_be_visible()