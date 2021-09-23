from mongoengine import *

class Borrower(Document):
    borrower_id = StringField(max_length=20)
    name = StringField(max_length=100)
    phone = StringField(max_length=15)

    # def __init__(self, id, name):
    #     self.id = id
    #     self.name = name
    #
    # def __str__(self):
    #     return "(" + self.id + ", " + self.name + ")"

    # def create_member(self):
    #
    # def remove_member(self):