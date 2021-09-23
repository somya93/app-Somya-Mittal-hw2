from model.Borrower import Borrower
from model.Book import Book


def process_input(user_input: str, borrower_id: str, book_id: str):
    book = Book.objects(book_id=book_id).first()
    if user_input == "checkout":
        if book.checked_out == "Y":
            print("\'" + book.title + "\' is already checked out by someone.")
            return
        book.borrower_id = borrower_id
        book.borrower_name = Borrower.objects(borrower_id=borrower_id).first().name
        book.checked_out = "Y"
        book.save()
        print("\'" + book.borrower_name + "\' has checked out \'" + book.title + "\'")
    else:
        # return a book command
        borrower_name = Borrower.objects(borrower_id=borrower_id).first().name
        if book.checked_out == "N":
            print(book_id + " is not currently checked out.")
            return
        if book.borrower_id != borrower_id:
            print("\'" + borrower_name + "\' has not currently checked out \'" + book.title + "\'")
            return
        book.borrower_id = ""
        book.borrower_name = ""
        book.checked_out = "N"
        book.save()
        print("\'" + borrower_name + "\' has returned \'" + book.title + "\'")


