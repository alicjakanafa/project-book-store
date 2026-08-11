class Author:
    def __init__(self, id, title, author, year):
        self.id = id
        self.title = title
        self.author = author
        self.year = year

    def __eq__(self, other):
        return (
            isinstance(other, Author)
            and self.id == other.id
            and self.title == other.title
            and self.author == other.author
            and self.year == other.year
        )

    def __repr__(self):
        return (
            f"Author({self.id}, {self.title}, "
            f"{self.author}, {self.year})"
        )