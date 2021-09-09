from controller import LMSController
from model.Book import Book
from model.Member import Member

# storing initial data
books = [Book("A234", "The 101 Dalmations"), Book("A675", "The 101 Dalmations"), Book("A212", "The 101 Dalmations"),
         Book("B671", "Charlie and the Chocolate Factory"), Book("B534", "Charlotte's Web"),
         Book("B777", "A Christmas Carol"),
         Book("B778", "Dracula"), Book("B812", "A Farewell to Arms"), Book("C101", "The Firm"),
         Book("C102", "War and Peace")]

members = [Member("L34", "Andrea Selleck"), Member("L22", "Lucas Hyatt"), Member("L19", "Carol Leonard"),
           Member("L84", "Ayesha Ford"), Member("L77", "Kenneth Trout")]


def verify_borrower(borrower_id: str, members: list):
    for member in members:
        if borrower_id == member.id:
            return True
    return False


def verify_book(book_id: str, books: list):
    for book in books:
        if book_id == book.id:
            return True
    return False


if __name__ == '__main__':
    main_prompt = "Enter \"checkout\" if you want to check out a book. \n Enter \"return\" if you want to return a book. \n" \
                  "Enter \"exit\" if you want to exit the application.\n"
    book_to_borrower_map = {}

    print("=================== Welcome to the Library Management System ===================")
    user_input = input(main_prompt)

    while user_input != "exit":
        if user_input == "checkout" or user_input == "return":
            prompt = "Please enter borrower's ID: "
            borrower_id = input(prompt)
            if not verify_borrower(borrower_id, members):
                print(borrower_id + " is not a valid borrower.")
                user_input = ""
                continue
            prompt = "Please enter the book ID: "
            book_id = input(prompt)
            if not verify_book(book_id, books):
                print("There is no such book " + book_id)
                user_input = ""
                continue
            LMSController.process_input(user_input, borrower_id, book_id, book_to_borrower_map)
        user_input = input(main_prompt)
