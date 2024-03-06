from lib.books import Books
from lib.book_repository import BookRepository

"""
When I call all
I get all books
"""

def test_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    result = repository.all()
    assert result == [
        Books(1,'Nineteen Eighty-Four', 'George Orwell'),
        Books(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Books(3, 'Emma', 'Jane Austen'),
        Books(4, 'Dracula', 'Bram Stoker'),
        Books(5, 'The Age of Innocence', 'Edith Wharton')]