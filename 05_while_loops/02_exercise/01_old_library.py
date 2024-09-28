favorite_book = input()

book = input()
checked_books = 0

while book != "No More Books" and book != favorite_book:
    checked_books += 1
    book = input()

if book == "No More Books":
    print(f"The book you search is not here!\nYou checked {checked_books} books.")
elif book == favorite_book:
    print(f"You checked {checked_books} books and found it.")