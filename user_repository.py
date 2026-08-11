from user import User


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            "SELECT * FROM users ORDER BY id"
        )

        users = []

        for row in rows:
            user = User(
                row["username"],
                row["password"],
                row["id"]
            )
            users.append(user)

        return users

    # def find(self, user_id):
    #     rows = self._connection.execute(
    #         "SELECT * FROM users WHERE id = %s",
    #         [user_id]
    #     )

    #     row = rows[0]

    #     return User(
    #         row["id"],
    #         row["username"],
    #         row["password"],
    #     )

    def create(self, user):
        self._connection.execute(
            """
            INSERT INTO users (username, password, year)
            VALUES (%s, %s, %s)
            """,
            [
                user.username,
                user.password,
            ]
        )

        return None

    # def delete(self, user_id):
    #     self._connection.execute(
    #         "DELETE FROM users WHERE id = %s",
    #         [user_id]
    #     )

    #     return None