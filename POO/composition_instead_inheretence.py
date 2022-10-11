# Inheritance approach
# class BookShelf: 
#     def __init__(self, quantity):
#         self.quantity = quantity

#     def __str__(self):
#         return f"Bookshelf with {self.quatity} books"

# shelf = BookShelf()

# class Book(BookShelf):
#     def __init__(self, name, quantity):
#         super.().__init__(quantity)
#         self.name = name
#     def __str__(self):
#         return f"Book {self.name}"

# book = Book("HarryPotter, 120")
# print(book)
#Composotino means to use one clase as argment to other and make them interact
#what about type?
#Composition approach 
class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BoookShelf with {len(self.books)} books"


class Book:
    def __init__(self, name):
        self.name = name 
    def __str__(self):
        return f"Book {self.name}"

book1 = Book("nook 1")
book2 = Book("nook 2")

shelf = BookShelf(book1, book2)
    