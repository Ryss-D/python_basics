class ClassTest():
    def intance_method(self):
        print("random priint")

    @classmethod
    # they uaully as used as facotryes to create objects
    # Its like a way to compensate the inexistence of named constructor
    # or multiple ocnstuctors in python
    def class_method(cls):
        print("random print")

    @staticmethod
    def static_methods():
        print("random print")


test = ClassTest()


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weigth

    def __repr__(self):
        return f"< Book {self.name}, {self.book_type}, weighing {self.weight}g >"

    @classmethod
    # cls reference the class
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)
