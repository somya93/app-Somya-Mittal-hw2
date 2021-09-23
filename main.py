from controller import LMSController
from model.Book import Book
from model.Borrower import Borrower
from mongoengine import *


# storing initial data
def reset(db_connection, database_name):
    db_connection.drop_database(database_name)
    initializeBorrowers()
    initializeBooks()
    print("Data has been reset")


def initializeBorrowers():
    borrower0 = Borrower(borrower_id="L34", name="Andrea Selleck", phone="639-555-1239")
    borrower1 = Borrower(borrower_id="L22", name="Lucas Hyatt", phone="408-555-2365")
    borrower2 = Borrower(borrower_id="L19", name="Carol Leonard", phone="650-555-8921")
    borrower3 = Borrower(borrower_id="L84", name="Ayesha Ford", phone="415-555-2120")
    borrower4 = Borrower(borrower_id="L77", name="Kenneth Trout", phone="510-555-1982")

    borrower0.save()
    borrower1.save()
    borrower2.save()
    borrower3.save()
    borrower4.save()

def initializeBooks():
    book0 = Book(book_id="A234", title="The 101 Dalmations", author="Dodie Smith", checked_out="N")
    book1 = Book(book_id="A675", title="The Adventures of Huckleberry Finn", author="Mark Twain", checked_out="N")
    book2 = Book(book_id="A212", title="Bag of Bones", author="Stephen King", checked_out="N")
    book3 = Book(book_id="B671", title="Charlie and the Chocolate Factory", author="Roald Dahl", checked_out="N")
    book4 = Book(book_id="B534", title="Charlotte's Web", author="E.B.White", checked_out="N")
    book5 = Book(book_id="B777", title="A Christmas Carol", author="Charles Dickens", checked_out="N")
    book6 = Book(book_id="B778", title="Dracula", author="Bram Stoker", checked_out="N")
    book7 = Book(book_id="B812", title="A Farewell to Arms", author="Ernest Hemingway", checked_out="N")
    book8 = Book(book_id="C101", title="The Firm", author="John Grisham", checked_out="N")

    book0.save()
    book1.save()
    book2.save()
    book3.save()
    book4.save()
    book5.save()
    book6.save()
    book7.save()
    book8.save()


def print_books():
    print("book_id \t title \t author \t checked_out \t borrower_id \t borrower_name")
    for each_data in Book.objects:
        print(each_data.book_id + "\t" + each_data.title + "\t" + each_data.author + "\t" + each_data.checked_out + "\t" + str(each_data.borrower_id) + "\t" + str(each_data.borrower_name))


def verify_borrower(borrower_id: str):
    borrowers = Borrower.objects(borrower_id=borrower_id)
    if not borrowers:
        return False
    return True


def verify_book(book_id: str):
    books = Book.objects(book_id=book_id)
    if not books:
        return False
    return True


if __name__ == '__main__':
    prompt = "Enter a database name:"
    database_name = input(prompt)
    if database_name == "":
        database_name = "app-somyam"
    db_connection = connect(database_name)

    main_prompt = "Enter a command:"
    user_input = input(main_prompt)

    while user_input != "exit":
        if user_input == "reset":
            reset(db_connection, database_name)
        if user_input == "books":
            print_books()
        if user_input == "checkout" or user_input == "return":
            prompt = "Enter Borrower Id: "
            borrower_id = input(prompt)
            if not verify_borrower(borrower_id):
                print("Borrower with Id " + borrower_id + " does not exist")
                user_input = ""
                continue
            prompt = "Enter Book Id:"
            book_id = input(prompt)
            if not verify_book(book_id):
                print("Book with Id " + book_id + " does not exist")
                user_input = ""
                continue
            LMSController.process_input(user_input, borrower_id, book_id)
        user_input = input(main_prompt)

    print("Exiting")
