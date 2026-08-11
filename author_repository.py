from author import Author


class AuthorRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            "SELECT * FROM authors ORDER BY id"
        )

        authors = []

        for row in rows:
            author = Author(
                row["id"],
                row["title"],
                row["author"],
                row["year"]
            )
            authors.append(author)

        return authors

    # def find(self, author_id):
    #     rows = self._connection.execute(
    #         "SELECT * FROM authors WHERE id = %s",
    #         [author_id]
    #     )

    #     row = rows[0]

    #     return Author(
    #         row["id"],
    #         row["title"],
    #         row["author"],
    #         row["year"]
    #     )

    # def create(self, author):
    #     self._connection.execute(
    #         """
    #         INSERT INTO authors (title, author, year)
    #         VALUES (%s, %s, %s)
    #         """,
    #         [
    #             author.title,
    #             author.author,
    #             author.year
    #         ]
    #     )

    #     return None

    # def delete(self, author_id):
    #     self._connection.execute(
    #         "DELETE FROM authors WHERE id = %s",
    #         [author_id]
    #     )

    #     return None