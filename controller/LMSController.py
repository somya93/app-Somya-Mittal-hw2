def process_input(user_input: str, borrower_id: str, book_id: str, book_to_borrower_map: dict):
    if user_input == "checkout":
        if book_id in book_to_borrower_map:
            # book is checked out to somebody else
            print(book_id + " is already checked out.")
            return
        book_to_borrower_map[book_id] = borrower_id
        print("Checkout successful!")
    else:
        # return a book command
        if not book_id in book_to_borrower_map:
            print(book_id + " is not currently checked out.")
            return
        if book_to_borrower_map[book_id] != borrower_id:
            print(book_id + " is not checked out by borrower " + borrower_id)
            return
        del book_to_borrower_map[book_id]
        print("Return successful!")


