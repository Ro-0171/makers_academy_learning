from lib.books import Books
"""
Construct an id, book title and author name

"""

def test_construct():
    book = Books(1 , "Nineteen Eighty-Four", "George Orwell")
    assert book.id == 1
    assert book.title == "Nineteen Eighty-Four"
    assert book.author_name == "George Orwell"

"""
Format books into strings
"""

def test_book_format():
    book = Books(1 , "Nineteen Eighty-Four", "George Orwell")
    assert str(book) == "Book 1, Nineteen Eighty-Four, George Orwell"


"""
Test books are equal
"""

def test_books_are_equal():
    book1 = Books(1, "Nineteen Eighty-Four", "George Orwell")
    book2 = Books(1, "Nineteen Eighty-Four", "George Orwell")
    assert book1 == book2