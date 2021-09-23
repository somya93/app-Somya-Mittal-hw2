from mongoengine import *


class Book(Document):
    book_id = StringField(max_length=20)
    title = StringField(max_length=100)
    author = StringField(max_length=100)
    checked_out = StringField(max_length=1)
    borrower_id = StringField(max_length=20)
    borrower_name = StringField(max_length=100)

    #
    # def __init__(self, id, title):
    #     self.id = id
    #     self.title = title
    #
    # def __str__(self):
    #     return "(" + self.id + ", " + self.title + ")"
    # def add_book(self):
    #
    # def remove_book(self):


