class Member:
    id: str
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "(" + self.id + ", " + self.name + ")"

    # def create_member(self):
    #
    # def remove_member(self):