

class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
    def describe(self):
        return f"'{self.name}' by '{self.author}', pages"
    def is_long(self):
        if self.pages >= 300:
            return True
        return False
book1 = Book("1984", "George Orwell", 328)
book2 = Book("The great Gatsby", "F. scott F", 180)


print(book1.describe())
print(book2.describe())

print(f"Is '{book1.name}' a long book? {book1.is_long()}")
print(f"Is '{book2.name}' a long book? {book2.is_long()}")