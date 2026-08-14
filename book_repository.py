from book import Book


class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            "SELECT * FROM books ORDER BY id"
        )

        books = []

        for row in rows:
            book = Book(
                row["title"],
                row["author"],
                row["year"],
                row["id"]
            )
            books.append(book)

        return books

    # def find(self, book_id):
    #     rows = self._connection.execute(
    #         "SELECT * FROM books WHERE id = %s",
    #         [book_id]
    #     )

    #     row = rows[0]

    #     return Book(
    #         row["id"],
    #         row["title"],
    #         row["author"],
    #         row["year"]
    #     )

    def create(self, book):
        self._connection.execute(
            """
            INSERT INTO books (title, author, year)
            VALUES (%s, %s, %s)
            """,
            [
                book.title,
                book.author,
                book.year
            ]
        )

        return None

    # def delete(self, book_id):
    #     self._connection.execute(
    #         "DELETE FROM books WHERE id = %s",
    #         [book_id]
    #     )

    #     return None

    def search(self, title="", author="", year=""):
        query = """
            SELECT * FROM books
            WHERE 1=1
        """

        params = []

        if title:
            query += " AND title ILIKE %s"
            params.append(f"%{title}%")

        if author:
            query += " AND author ILIKE %s"
            params.append(f"%{author}%")

        if year:
            query += " AND year = %s"
            params.append(year)

        query += " ORDER BY id"

        rows = self._connection.execute(query, params)

        books = []

        for row in rows:
            books.append(
                Book(
                    row["title"],
                    row["author"],
                    row["year"],
                    row["id"]
                )
            )

        return books