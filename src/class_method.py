class Book:
    count = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author

        Book.count += 1

    @classmethod
    def get_book_count(cls):
        return cls.count

    @classmethod
    def create(cls, title, author):
        return cls(title, author)

book_1 = Book.create("title 1", "A")
book_2 = Book.create("title 2", "B")

print(Book.get_book_count())
