class User:
    def __init__(self, username, password, id = None):
        self.id = id
        self.username = username
        self.password = password

    def __eq__(self, other):
        return (
            isinstance(other, User)
            and self.id == other.id
            and self.username == other.username
            and self.password == other.password
        )

    def __repr__(self):
        return (
            f"User({self.id}, {self.username}, "
            f"{self.password})"
        )