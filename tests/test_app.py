import sys
import os

# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

# a descriptive test name
def test_get_books_returns_a_200():
    # here's where we make the test client
    client = app.test_client()

    # here's where we make the request
    response = client.get("/books")

    # here's where we assert that the response's status code is 200
    assert response.status_code == 200

# a descriptive test name
def test_books_page_displays_all_books():
    client = app.test_client()

    response = client.get("/books")

    assert response.status_code == 200
    assert b"The Great Gatsby" in response.data
    assert b"To Kill a Mockingbird" in response.data
    assert b"1984" in response.data
    assert b"Pride and Prejudice" in response.data
    assert b"The Catcher in the Rye" in response.data
    
def test_get_authors_returns_200():
    client = app.test_client()

    response = client.get("/authors")

    assert response.status_code == 200

def test_get_authors_returns_all_authors():

    client = app.test_client()
    response = client.get("/authors")

    assert response.json == [
        {
            "name": "F. Scott Fitzgerald",
            "dob": "1896-09-24"
        },
        {
            "name": "Harper Lee",
            "dob": "1926-04-28"
        },
        {
            "name": "George Orwell",
            "dob": "1903-06-25"
        },
        {
            "name": "Jane Austen",
            "dob": "1775-12-16"
        },
        {
            "name": "J.D. Salinger",
            "dob": "1919-01-01"
        }
    ]