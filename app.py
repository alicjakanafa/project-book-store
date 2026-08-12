from flask import Flask, render_template, request, redirect, session
from database_connection import DatabaseConnection
from book_repository import BookRepository, Book
from user_repository import UserRepository, User
from login_required import *

# instantiate a Flask app object
app = Flask(__name__)
app.secret_key = "some_really_secret_key"

@app.route("/books", methods=['GET'])
def get_books_page():

  connection = DatabaseConnection()
  connection.connect()
  book_repository = BookRepository(connection)
  books = book_repository.all()
  return render_template("books.html", books=books)

@app.route("/books", methods=['POST'])
@login_required
def add_book():
  connection = DatabaseConnection()
  connection.connect()
  book_repository = BookRepository(connection)
  book_details = request.form
  book = Book(title=book_details["title"], author=book_details["author"], year=book_details["year"])
  book_repository.create(book)
  return redirect("/books")

@app.route('/authors', methods=['GET'])
def get_authors():
    return [
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

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/users/new', methods=['GET'])
def get_signup_form():
    return render_template("signup.html")

@app.route('/users', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form
    user = User(username=user_details["username"], password=user_details["password"])
    user_repository.create(user)
    return redirect("/books")

@app.route('/sessions/new', methods=['GET'])
def get_login_form():
    return render_template("login.html")

@app.route('/sessions', methods=['POST'])
def create_session():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)

    username = request.form["username"]
    password = request.form["password"]

    user = user_repository.find_by_username(username)

    if user and user.password == password:
        session["user_id"] = user.id
        session["username"] = user.username
        return redirect("/books")
    else:
        return redirect("/sessions/new")

# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)