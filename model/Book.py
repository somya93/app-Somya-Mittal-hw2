class Book:
    id: str
    title: str

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __str__(self):
        return "(" + self.id + ", " + self.title + ")"
    # def add_book(self):
    #
    # def remove_book(self):


